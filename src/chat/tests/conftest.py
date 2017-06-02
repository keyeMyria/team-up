import pytest

from common.generators import generate_room, generate_message


@pytest.fixture
def room():
    return generate_room()


@pytest.fixture
def message(normal_user, room):
    generate_message(user=normal_user, room=room)
