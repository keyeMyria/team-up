from channels.db import database_sync_to_async

from common.exceptions import ClientError
from chatter.models import Room, Message, ChatEvent


# This decorator turns this function from a synchronous function into an async one
# we can call from our async consumers, that handles Django DBs correctly.
# For more, see http://channels.readthedocs.io/en/latest/topics/databases.html
@database_sync_to_async
def get_room_or_error(room_id, user):
    """
    Tries to fetch a room for the user, checking permissions along the way.
    """
    # Check if the user is logged in
    if not user.is_authenticated:
        raise ClientError('USER_HAS_TO_LOGIN')
    # Find the room they requested (by ID)
    try:
        room = Room.objects.get(pk=room_id)
    except Room.DoesNotExist:
        raise ClientError('ROOM_INVALID')
    # Check permissions
    if not room.allowed(user):
        raise ClientError('ROOM_ACCESS_DENIED')
    return room


@database_sync_to_async
def save_message(room_id, user, message):
    return Message.objects.create(room_id=room_id, sender=user, content=message)


@database_sync_to_async
def add_chat_event(event, user, room):
    return ChatEvent.objects.create(event=event, user=user, room_id=room)
