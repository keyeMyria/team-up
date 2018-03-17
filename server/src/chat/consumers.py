from channels.generic.websocket import AsyncJsonWebsocketConsumer

from common.exceptions import ClientError
from chat.utils import get_room_or_error, save_message, add_chat_event


class ChatConsumer(AsyncJsonWebsocketConsumer):
    """
    This chat consumer handles websocket connections for chat clients.

    It uses AsyncJsonWebsocketConsumer, which means all the handling functions
    must be async functions, and any sync work (like ORM access) has to be
    behind database_sync_to_async or sync_to_async. For more, read
    http://channels.readthedocs.io/en/latest/topics/consumers.html
    """

    async def connect(self):
        """
        Called when the websocket is handshaking as part of initial connection.
        """
        self.user = self.scope['user']
        if self.user is None or not self.user.is_authenticated:
            await self.close()
        else:
            await self.accept()
        self.rooms = set()

    async def receive_json(self, content, **kwargs):
        """
        Called when we get a text frame. Channels will JSON-decode the payload
        for us and pass it as the first argument.
        """
        command = content.get('command', None)
        try:
            if command == 'join':
                await self.join_room(content['room'])
            elif command == 'leave':
                await self.leave_room(content['room'])
            elif command == 'send':
                await self.send_room(content['room'], content['message'])
        except ClientError as e:
            await self.send_json({'error': e.code})

    async def disconnect(self, code):
        """
        Called when the WebSocket closes for any reason.
        """
        for room_id in list(self.rooms):
            try:
                await self.leave_room(room_id)
                await add_chat_event('disconnect', self.user, room_id)
            except ClientError:
                pass

    async def join_room(self, room_id):
        """
        Called by receive_json when someone sent a join command.
        """
        room = await get_room_or_error(room_id, self.user)
        await self.channel_layer.group_send(
            room.name,
            {
                'type': 'chat.join',
                'room_id': room_id,
                'username': self.user.username,
            }
        )
        self.rooms.add(room_id)
        await self.channel_layer.group_add(
            room.name,
            self.channel_name,
        )
        await self.send_json({
            'join': str(room.id),
            'name': room.name,
        })
        await add_chat_event('connect', self.user, room_id)

    async def leave_room(self, room_id):
        """
        Called by receive_json when someone sent a leave command.
        """
        room = await get_room_or_error(room_id, self.user)
        await self.channel_layer.group_send(
            room.name,
            {
                'type': 'chat.leave',
                'room_id': room_id,
                'username': self.scope['user'].username,
            }
        )
        self.rooms.discard(room_id)
        await self.channel_layer.group_discard(
            room.name,
            self.channel_name,
        )
        await self.send_json({
            'leave': str(room.id),
        })

    async def send_room(self, room_id, message):
        """
        Called by receive_json when someone sends a message to a room.
        """
        # Check they are in this room
        if room_id not in self.rooms:
            raise ClientError('ROOM_ACCESS_DENIED')
        # Get the room and send to the group about it
        room = await get_room_or_error(room_id, self.user)
        await self.channel_layer.group_send(
            room.name,
            {
                'type': 'chat.message',
                'room_id': room_id,
                'username': self.user.username,
                'message': message,
            }
        )
        await save_message(room_id, self.user, message)


    # These helper methods are named by the types we send - so chat.join becomes chat_join
    async def chat_join(self, event):
        """
        Called when someone has joined our chat.
        """
        # Send a message down to the client
        await self.send_json(
            {
                'msg_type': 'ENTER',
                'room': event['room_id'],
                'username': event['username'],
            },
        )

    async def chat_leave(self, event):
        """
        Called when someone has left our chat.
        """
        # Send a message down to the client
        await self.send_json(
            {
                'msg_type': 'LEAVE',
                'room': event['room_id'],
                'username': event['username'],
            },
        )

    async def chat_message(self, event):
        """
        Called when someone has messaged our chat.
        """
        # Send a message down to the client
        await self.send_json(
            {
                'msg_type': 'MESSAGE',
                'room': event['room_id'],
                'username': event['username'],
                'message': event['message'],
            },
        )
