import pytest
from channels.test import HttpClient

from chat.models import Room, Message


@pytest.fixture
def client():
    return HttpClient()


def get_path(room_id):
    return f'/chat/{room_id}/'


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


def get_connected_client(client, room, path, base_content, normal_user):
    room.save()
    room.users.add(normal_user)
    content = base_content
    client.send('websocket.connect', path=path, content=content)
    client.consume('websocket.connect', fail_on_none=True)
    client.receive()
    return client


@pytest.fixture
def connected_client(client, room, path, base_content, normal_user):
    return get_connected_client(client, room, path, base_content, normal_user)


class TestChatConsumerConnect:
    def test_connect(self, connected_client):
        pass

    def test_connect_not_allowed(self, client, base_content, path):
        content = base_content
        client.send('websocket.connect', path=path, content=content)
        with pytest.raises(AssertionError):  # '{accept: True}' not received
            client.consume('websocket.connect', fail_on_none=True)

    def test_no_token(self, client, path, room, normal_user):
        room.save()
        room.users.add(normal_user)
        client.send('websocket.connect', path=path)
        with pytest.raises(AssertionError):  # '{accept: True}' not received
            client.consume('websocket.connect', fail_on_none=True)

    def test_not_existing_room(self, client, base_content, room, normal_user):
        room.save()
        room.users.add(normal_user)
        not_existing_room_id = Room.objects.latest('id').id + 1
        path = get_path(not_existing_room_id)
        client.send('websocket.connect', path=path, content=base_content)
        with pytest.raises(AssertionError):  # '{accept: True}' not received
            client.consume('websocket.connect', fail_on_none=True)

    def test_active_in_room(self, connected_client, room, normal_user):
        assert normal_user.active_rooms.filter(id=room.id).exists()


class TestChatConsumerReceive:
    def test_receive_message(self, connected_client: HttpClient, path):
        connected_client.send_and_consume('websocket.receive',
                                          text={'content': {'message': 'hey'}},
                                          path=path)
        assert connected_client.receive()

    @pytest.mark.django_db
    def test_message_object_create(self, connected_client: HttpClient, path, room, normal_user):
        message = 'hey'
        connected_client.send_and_consume('websocket.receive',
                                          text={'content': {'message': message}},
                                          path=path)
        assert Message.objects.filter(room_id=room.id, sender=normal_user,
                                      content=message).count() == 1


class TestChatConsumerDisconnect:
    def test_not_active(self, connected_client: HttpClient, path, normal_user, room):
        connected_client.send_and_consume('websocket.disconnect',
                                          path=path)
        assert not normal_user.active_rooms.filter(id=room.id).exists()
