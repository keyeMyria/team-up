import pytest

from django.core.urlresolvers import reverse
from django.test import Client

from common.generators import generate_league_of_legends_account_data
from common.testing import BaseViewTest
from games.models import LeagueOfLegendsAccount


class BaseTestAccountViewSet(BaseViewTest):
    view_name = ''
    gen_func = None
    model = None

    @pytest.fixture
    def new_acc_data(self):
        return self.gen_func()

    def test_can_create_account(self, client: Client, normal_user_auth, list_url, new_acc_data):
        """
        POST /api/games/<game>/
        Testing creating new game account as a normal user.
        """
        response = client.post(list_url, new_acc_data, **normal_user_auth)
        assert response.status_code == 201

    def test_can_retrieve_account(self, client: Client, normal_user_auth, league_acc):
        """
        GET /api/games/<game>/{id}/
        Testing retrieving game account as a normal user.
        """
        print(league_acc.detail_url)
        response = client.get(league_acc.detail_url, **normal_user_auth)
        assert response.status_code == 200

    def test_can_delete_account(self, client: Client, normal_user_auth, league_acc):
        """
        DELETE /api/games/<game>/{id}/
        Testing deleting game account details as a normal user.
        """
        print(league_acc.detail_url)
        response = client.delete(league_acc.detail_url, **normal_user_auth)
        assert response.status_code == 204


class TestLeagueOfLegendsAccountViewSet(BaseTestAccountViewSet):
    view_name = 'api:games:league_of_legends'
    gen_func = generate_league_of_legends_account_data
    model = LeagueOfLegendsAccount

    def test_cannot_create_duplicate_account(self, client: Client, normal_user_auth, list_url,
                                             league_acc):
        """
        POST /api/games/league/
        Ensure we cannot create a duplicate of an account as a normal user.
        """
        response = client.post(list_url, league_acc.existing_acc_data, **normal_user_auth)
        assert response.status_code == 400
        error_message = 'The fields username, server must make a unique set.'
        assert error_message in response.data['non_field_errors']
