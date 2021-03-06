import pytest
from typing import Optional, Union
from django.urls import reverse
from channels.testing import WebsocketCommunicator, ApplicationCommunicator

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
        return reverse(f'{self.settings_class.view_name}-list')


class QSWebsocketCommunicator(WebsocketCommunicator):
    def __init__(self, application, path, headers=None, subprotocols=None,
                 query_string: Optional[Union[str, bytes]]=None):
        if isinstance(query_string, str):
            query_string = str.encode(query_string)
        self.scope = {
            "type": "websocket",
            "path": path,
            "headers": headers or [],
            "subprotocols": subprotocols or [],
            "query_string": query_string or ''
        }
        ApplicationCommunicator.__init__(self, application, self.scope)
