import pytest

from common.generators import generate_chat_event, generate_message, generate_room


@pytest.fixture
def room():
    room = generate_room()
    room.save()
    return room


@pytest.fixture
def room_with_user(room, normal_user):
    room.users.add(normal_user)
    yield room
    room.users.remove(normal_user)


@pytest.fixture
def message(normal_user, room):
    return generate_message(user=normal_user, room=room)


@pytest.fixture
def chat_event(normal_user, room):
    return generate_chat_event(user=normal_user, room=room)
