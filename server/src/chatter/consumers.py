from channels.generic.websocket import JsonWebsocketConsumer
from django.core.exceptions import ObjectDoesNotExist

from chatter.models import Room, ChatEvent, Message


class ChatConsumer(JsonWebsocketConsumer):
    groups = ["broadcast"]

    def connect(self):
        # Called on connection. Either call
        self.accept()

        self.user = self.scope['user']
        self.room_id = self.scope['url_route']['room_id']
        group = f'room_{self.room_id}'
        self.group_name = group

        if not (self.user is not None and self.user.is_authenticated()):
            return self.close({'Error': 'Not authenticated user'})

        try:
            room = Room.objects.get(id=self.room_id)
            self.room = room
        except ObjectDoesNotExist:
            return self.close({'Error': 'Room does not exists'})

        # Send success response
        self.accept()

        # Save user as active
        self.room.active_users.add(self.user)

        # Send information about new connection
        connect_message = f'{self.user.username} joined the chat'
        self.channel_layer.group_send(group, connect_message)

        # Add user to group
        self.channel_layer.group_add(group, self.channel_name)

        # Log chat event
        self.add_chat_event('connect')

    def receive_json(self, content, **kwargs):
        # Called with either text_data or bytes_data for each frame
        # You can call:
        self.send_json({'data': content})
        """
        Called when a message is received with decoded JSON content
        """
        # Send message to other users
        message = content['message']
        self.channel_layer.group_send(self.group_name, f'{self.user.username}: {message}')

        # Save message object in db
        Message.objects.create(room_id=self.room_id, sender=self.user, content=message)

    def disconnect(self, close_code):
        # Remove user from group
        self.channel_layer.group_discard(self.group_name, self.channel_name)
        # Send information about disconnect to the group
        disconnect_message = f'{self.user.username} disconnected'
        self.channel_layer.group_send(self.group_name, disconnect_message)

        # Remove user from active users in room
        self.room.active_users.remove(self.user)

        # Log chat event
        self.add_chat_event('disconnect')

    def add_chat_event(self, event):
        return ChatEvent.objects.create(event=event, user=self.user, room=self.room)
