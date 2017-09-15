import pytest

from common.generators import generate_chat_event, generate_message, generate_room


@pytest.fixture
def room():
    return generate_room()


@pytest.fixture
def message(normal_user, room):
    return generate_message(user=normal_user, room=room)


@pytest.fixture
def chat_event(normal_user, room):
    return generate_chat_event(user=normal_user, room=room)
