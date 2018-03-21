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


async def get_connected_communicator(temp_token) -> QSWebsocketCommunicator:
    communicator = QSWebsocketCommunicator(application, '/chat/', query_string=get_query_string(temp_token))
    connected, subprotocol = await communicator.connect()
    if not connected:
        communicator.disconnect()
        raise AssertionError
    return communicator


@pytest.fixture
async def connected_communicator(temp_token):
    communicator = await get_connected_communicator(temp_token)
    yield communicator
    await communicator.disconnect()


@pytest.mark.django_db(transaction=True)
class TestConnect:
    @pytest.mark.asyncio
    async def test_get_connected_client(self, connected_communicator):
        pass

    @pytest.mark.asyncio
    async def test_connect_not_allowed(self):
        class MockToken:
            token = 'wrong'
        with pytest.raises(AssertionError):
            await get_connected_communicator(MockToken())


@pytest.mark.django_db(transaction=True)
class TestChatCommunicator:
    @pytest.mark.asyncio
    async def test_wrong_command(self, connected_communicator):
        await connected_communicator.send_json_to({'command': 'not_real_command'})
        response = await connected_communicator.receive_json_from()
        assert 'error' in response

    # @pytest.mark.asyncio
    # async def test_join_room(self, connected_communicator, room_with_user, normal_user):
    #     await connected_communicator.send_json_to({'command': 'join', 'room': room_with_user.id})
    #     response = await connected_communicator.receive_json_from()
    #     assert response == {'join': str(room_with_user.id), 'name': room_with_user.name}
    #     assert normal_user in room_with_user.users.all()

    # @pytest.mark.asyncio
    # async def test_send_message(self, connected_communicator, room_with_user):
    #     await connected_communicator.send_json_to({'command': 'join', 'room': room_with_user.id})
    #     response = await connected_communicator.receive_json_form()
    #     assert response == {'join': str(room_with_user.id), 'name': room_with_user.name}
    #
    # @pytest.mark.asyncio
    # async def test_join_room(self, connected_communicator, room_with_user):
    #     await connected_communicator.send_json_to({'command': 'join', 'room': room_with_user.id})
    #     response = await connected_communicator.receive_json_form()
    #     assert response == {'join': str(room_with_user.id), 'name': room_with_user.name}