import pytest
from channels.testing import WebsocketCommunicator

from chatter.consumers import ChatConsumer
from config.routing import application


def get_path(room_id):
    return f'/chat/{room_id}/'


@pytest.fixture
def communicator(path):
    communicator = WebsocketCommunicator(application, path)
    return communicator


@pytest.fixture
def path(room):
    room.save()
    return get_path(room.id)


@pytest.fixture
def base_content(token):
    content = {
        'query_string': f'token={token}'
    }
    return content


@pytest.mark.asyncio
async def test_get_connected_client(communicator: WebsocketCommunicator, room, base_content, normal_user):
    room.save()
    room.users.add(normal_user)
    connected, subprotocol = await communicator.connect()
    assert connected