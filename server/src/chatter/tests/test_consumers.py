import pytest
from channels.testing import WebsocketCommunicator

from config.routing import application
from chatter.models import TemporaryToken


def get_path(room_id):
    return f'/chat/{room_id}/'


@pytest.fixture
def path(room):
    room.save()
    return get_path(room.id)


@pytest.fixture
def temp_token(normal_user):
    return TemporaryToken.generate(normal_user)


@pytest.mark.asyncio
async def test_get_connected_client(path, room, temp_token, normal_user):
    room.save()
    room.users.add(normal_user)

    #TODO: set query string with temp token
    communicator = WebsocketCommunicator(application, path)
    connected, subprotocol = await communicator.connect()
    assert connected
    await communicator.disconnect()

