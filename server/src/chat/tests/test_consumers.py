import pytest

from common.testing import QSWebsocketCommunicator
from config.routing import application
from chat.models import TemporaryToken


@pytest.fixture
def temp_token(normal_user):
    token = TemporaryToken.generate(normal_user)
    token.save()
    return token


def get_query_string(temp_token: TemporaryToken) -> str:
    return f'token={temp_token.token}'


@pytest.mark.django_db(transaction=True)
class TestConnect:

    @pytest.mark.asyncio
    async def test_get_connected_client(self, temp_token):

        communicator = QSWebsocketCommunicator(application, '/chat/', query_string=get_query_string(temp_token))
        connected, subprotocol = await communicator.connect()
        assert connected
        await communicator.disconnect()


    @pytest.mark.asyncio
    async def test_connect_not_allowed(self):
        class MockToken:
            token = 'wrong'
        communicator = QSWebsocketCommunicator(application, '/chat/', query_string=get_query_string(MockToken()))
        connected, subprotocol = await communicator.connect()

        assert not connected
        await communicator.disconnect()

