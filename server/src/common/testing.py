import pytest
from accounts.models import User
from django.core.urlresolvers import reverse

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
