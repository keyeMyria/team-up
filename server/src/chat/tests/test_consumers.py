import pytest

from common.testing import QSWebsocketCommunicator
from config.routing import application
from chat.models import TemporaryToken


def get_path(room_id) -> str:
    return f'/chat/{room_id}/'


@pytest.fixture
def path(room):
    return get_path(room.id)


@pytest.fixture
def temp_token(normal_user):
    token = TemporaryToken.generate(normal_user)
    token.save()
    return token


def get_query_string(temp_token: TemporaryToken) -> str:
    return f'token={temp_token.token}'


# @pytest.mark.django_db
# class TestConnect:
#
#     @pytest.mark.asyncio
#     async def test_get_connected_client(self, path, room_with_user, temp_token):
#         assert get_path(room_with_user.id) == path
#
#         communicator = QSWebsocketCommunicator(application, path, query_string=get_query_string(temp_token))
#         connected, subprotocol = await communicator.connect()
#         assert connected
#         await communicator.disconnect()

#
# @pytest.mark.asyncio
# async def test_connect_not_allowed(path, temp_token):
#     communicator = QSWebsocketCommunicator(application, path, query_string=get_query_string(temp_token))
#     connected, subprotocol = await communicator.connect()
#
#     assert not connected
#     await communicator.disconnect()

