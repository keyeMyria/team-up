import pytest

from django.core.urlresolvers import reverse
from django.test import Client

from common.generators import generate_league_of_legends_account_data
from common.testing import auth_headers
from accounts.models import User
from games.models import LeagueOfLegendsAccount


class BaseTestAccountViewSet:
    view_name = ''
    gen_func = None

    @pytest.fixture
    def normal_user_auth(self, normal_user: User):
        return auth_headers(normal_user)

    @pytest.fixture
    def admin_user_auth(self, admin_user: User):
        return auth_headers(admin_user)

    @pytest.fixture
    def list_url(self):
        return reverse(f'{self.view_name}-list')

    @pytest.fixture
    def new_acc_data(self):
        return self.gen_func()

    @pytest.fixture
    def _new_instance(self) -> dict:
        d = {}
        acc_data = self.gen_func()
        instance = LeagueOfLegendsAccount.objects.create(**acc_data)
        d['acc_data'] = acc_data
        d['instance'] = instance
        d['detail_url'] = reverse(f'{self.view_name}-detail', kwargs={'pk': instance.pk})
        return d

    @pytest.fixture
    def existing_acc_data(self, _new_instance: dict):
        return _new_instance['acc_data']

    @pytest.fixture
    def instance(self, _new_instance: dict):
        return _new_instance['instance']

    @pytest.fixture
    def detail_url(self, _new_instance: dict):
        return _new_instance['detail_url']

    def test_can_create_account(self, client: Client, normal_user_auth, list_url, new_acc_data):
        """
        POST /api/games/league/
        Testing creating new game account as a normal user.
        """
        response = client.post(list_url, new_acc_data, **normal_user_auth)
        assert response.status_code == 201

    def test_can_retrieve_account(self, client: Client, normal_user_auth, detail_url):
        """
        GET /api/games/league/{id}/
        Testing retrieving game account as a normal user.
        """
        response = client.get(detail_url, **normal_user_auth)
        assert response.status_code == 200

    def test_can_delete_account(self, client: Client, normal_user_auth, detail_url):
        """
        DELETE /api/games/league/{id}/
        Testing deleting game account details as a normal user.
        """
        response = client.delete(detail_url, **normal_user_auth)
        assert response.status_code == 204


class TestLeagueOfLegendsAccountViewSet(BaseTestAccountViewSet):
    view_name = 'api:games:league_of_legends'
    gen_func = generate_league_of_legends_account_data

    def test_cannot_create_duplicate_account(self, client: Client, normal_user_auth, list_url,
                                             existing_acc_data):
        """
        POST /api/games/league/
        Ensure we cannot create a duplicate of an account | normal user.
        """
        response = client.post(list_url, existing_acc_data, **normal_user_auth)
        assert response.status_code == 400
        assert 'The fields username, server must make a unique set.' in \
               response.data['non_field_errors']
