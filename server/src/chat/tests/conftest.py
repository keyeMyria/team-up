import pytest
from django.db import transaction

from accounts.models import User
from common.generators import generate_chat_event, generate_message, generate_room, generate_user


@pytest.fixture
def normal_user():
    with transaction.atomic():
        User.objects.all().delete()
        user = generate_user()
    return user


@pytest.fixture
def room():
    with transaction.atomic():
        room = generate_room()
        room.save()
    return room


@pytest.fixture
def room_with_user(room, normal_user):
    with transaction.atomic():
        room.users.add(normal_user)
    yield room
    with transaction.atomic():
        room.users.remove(normal_user)


@pytest.fixture
def message(normal_user, room):
    with transaction.atomic():
        message = generate_message(user=normal_user, room=room)
    return message


@pytest.fixture
def chat_event(normal_user, room):
    with transaction.atomic():
        chat_event = generate_chat_event(user=normal_user, room=room)
    return chat_event
