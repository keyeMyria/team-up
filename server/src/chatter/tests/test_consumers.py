import pytest
from common.testing import QSWebsocketCommunicator

from config.routing import application
from chatter.models import TemporaryToken
from channels.db import database_sync_to_async


def get_path(room_id):
    return f'/chat/{room_id}/'


@pytest.fixture
def path(room):
    room.save()
    return get_path(room.id)


@pytest.fixture
def temp_token(normal_user):
    return TemporaryToken.generate(normal_user)


@pytest.mark.django_db
@pytest.mark.asyncio
async def test_get_connected_client(path, room, temp_token, normal_user, db):
    await save(room, db)
    assert room.id == path
    room.users.add(normal_user)
    temp_token.save()

    #TODO: set query string with temp token
    communicator = QSWebsocketCommunicator(application, path, query_string=f'token={temp_token.token}')
    connected, subprotocol = await communicator.connect()
    assert connected
    await communicator.disconnect()


@database_sync_to_async
def save(room, db):
    return room.save()
