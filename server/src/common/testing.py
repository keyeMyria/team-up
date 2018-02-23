import pytest
from django.urls import reverse
from django.test.client import Client

from accounts.models import User
from common.utils import create_user_token


def auth_headers(user: User) -> dict:
    token = create_user_token(user=user)
    headers = {
        'Authorization': 'Bearer {}'.format(token)
    }
    return headers


class BaseViewTest:
    settings_class = None

    @pytest.fixture
    def normal_user_auth(self, normal_user: User):
        return auth_headers(normal_user)

    @pytest.fixture
    def admin_user_auth(self, admin_user: User):
        return auth_headers(admin_user)

    @pytest.fixture
    def list_url(self):
        return reverse(f'{self.settings_class.view_name}-list')[len('server/'):]


class CustomClient(Client):

    def __getattribute__(self, name):
        func = super().__getattribute__(name)
        methods_to_wrap = ['get', 'post', 'head', 'options', 'put', 'patch', 'delete', 'trace']
        if name in methods_to_wrap:
            return self._prepare_path(func)
        else:
            return func

    @staticmethod
    def _prepare_path(func):
        def wrapper(path, *args, **kwargs):
            if path.startswith('/server'):
                path = path[len('/server'):]
            return func(path, *args, **kwargs)
        return wrapper

