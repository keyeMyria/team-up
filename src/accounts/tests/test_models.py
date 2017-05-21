import pytest
from django.core.exceptions import ValidationError

from accounts.models import User, username_validator


class TestUserNameValidator:
    def test_valid_username(self):
        username_validator('abcde234')

    def test_long_username(self):
        username_validator('a'*15)

    def test_short_username(self):
        username_validator('a'*3)

    def test_too_long_username(self):
        with pytest.raises(ValidationError):
            username_validator('a'*16)

    def test_too_short_username(self):
        with pytest.raises(ValidationError):
            username_validator('a')

    def test_not_alphanumeric_username(self):
        with pytest.raises(ValidationError):
            username_validator('hdfg#@$*&((@')


class TestUserModel:
    @pytest.fixture
    def user(self):
        return User(username='ziemniak', email='ziemniak@ziemniak.com')

    def test_user(self, user):
        pass

    def test_short_name(self, user):
        assert user.get_short_name() == user.username
        user.first_name = 'someone'
        assert user.get_short_name() == user.first_name

    def test_full_name(self, user):
        assert user.get_full_name() == user.username
        user.first_name = 'someone'
        user.last_name = 'someone'
        assert user.get_full_name() == 'someone someone'


@pytest.mark.django_db
class TestUserManager:
    def test_create_user(self):
        email = 'something@c.c'
        user = User.objects.create_user(username='somehting', email=email)
        assert user == User.objects.get(email=email)

    def test_create_superuser(self):
        email = 'something@c.c'
        user = User.objects.create_superuser(username='somehting', email=email, password='test')
        assert user == User.objects.get(email=email)
        assert user.is_superuser
