from django.core.exceptions import ObjectDoesNotExist

from channels.generic.websockets import JsonWebsocketConsumer
from channels import Group

from chat.models import Room, Message, ChatEvent

from common.authentication import RestTokenConsumerMixin
from common.mixins import KeepUserConsumerMixin


class ChatConsumer(RestTokenConsumerMixin,
                   KeepUserConsumerMixin,
                   JsonWebsocketConsumer):

    def connect(self, message, room_id=None, **kwargs):
        """
        Perform things on connection start
        """

        if not (message.user is not None and message.user.is_authenticated()):
            return self.close({'Error': 'Not authenticated user'})

        # Ensure that given room exists
        try:
            room = Room.objects.get(id=room_id)
            self._room = room
        except ObjectDoesNotExist:
            return self.close({'Error': 'Room does not exists'})

        # Check if user is allowed to join it
        if not self.room.allowed(message.user):
            return self.close({'Error': 'User not allowed in this room'})

        # Send success response
        message.reply_channel.send({"accept": True})

        # Save user as active
        self.room.active_users.add(message.user)

        # Add needed information to channel_session
        group = f'room_{room_id}'
        message.channel_session['room_id'] = room_id
        message.channel_session['group_name'] = group

        # Send information about new connection
        connect_message = f'{message.user.username} joined the chat'
        self.group_send(group, connect_message)

        # Add user to group
        Group(group).add(message.reply_channel)

        # Log chat event
        self.add_chat_event('connect')

    def receive(self, content, **kwargs):
        """
        Called when a message is received with decoded JSON content
        """
        # Send message to other users
        message = content['content']['message']
        self.group_send(self.group_name, f'{self.user.username}: {message}')

        # Save message object in db
        Message.objects.create(room_id=self.room_id, sender=self.user, content=message)

    def disconnect(self, message, **kwargs):
        """
        Perform things on connection close
        """
        # Remove user from group
        Group(self.group_name).discard(message.reply_channel)
        # Send information about disconnect to the group
        disconnect_message = f'{self.user.username} disconnected'
        self.group_send(self.group_name, disconnect_message)

        # Remove user from active users in room
        self.room.active_users.remove(self.user)

        # Log chat event
        self.add_chat_event('disconnect')

    @property
    def group_name(self) -> str:
        if not hasattr(self, '_group_name'):
            self._group_name = self.message.channel_session['group_name']
        return self._group_name

    @property
    def room_id(self):
        if not hasattr(self, '_room_id'):
            self._room_id = self.message.channel_session['room_id']
        return self._room_id

    @property
    def room(self) -> Room:
        if not hasattr(self, '_room'):
            room_id = self.room_id
            self._room = Room.objects.get(id=room_id)
        return self._room

    def add_chat_event(self, event):
        return ChatEvent.objects.create(event=event, user=self.user, room=self.room)
