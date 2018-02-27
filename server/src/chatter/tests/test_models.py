import pytest

from common.generators import generate_message


@pytest.mark.django_db
class TestMessage:
    def test_creation(self, message):
        pass


class TestRoom:
    def test_creation(self, room):
        pass

    @pytest.mark.django_db
    def test_save(self, room):
        room.save()

    def test_last_activity_is_none_without_messages(self, room):
        assert room.last_activity is None

    @pytest.mark.django_db
    def test_last_activity_with_messages(self, room, normal_user):
        for _ in range(2):
            last_message = generate_message(room=room, user=normal_user)
            last_message.save()
        assert room.last_activity == last_message


@pytest.mark.django_db
class TestChatEvent:
    def test_creation(self, chat_event):
        pass
