import json
import pytest

from django.test import Client

from common.testing import BaseViewTest
from games.tests.conftest import LeagueOfLegendsSettings


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
        response = client.get(league_acc.detail_url, **normal_user_auth)
        assert response.status_code == 200

    def test_can_delete_account(self, client: Client, normal_user_auth, league_acc):
        """
        DELETE /api/games/<game>/{id}/
        Testing deleting game account details as a normal user.
        """
        response = client.delete(league_acc.detail_url, **normal_user_auth)
        assert response.status_code == 204

    @pytest.mark.parametrize("key, status_code", [
        ('username', 200),
        ('league', 200),
        ('division', 200),
        ('server', 200),
    ])
    def test_can_patch_update_account(self, client: Client, normal_user_auth, league_acc,
                                      new_acc_data, key, status_code):
        """
        PATCH /api/games/<game>/{id}/
        Testing patch updating game account details as a normal user.
        """
        data = {key: new_acc_data[key]}
        response = client.patch(league_acc.detail_url,
                                json.dumps(data),
                                content_type='application/json',
                                **normal_user_auth)
        assert response.status_code == status_code

    def test_can_put_update_account(self, client: Client, normal_user_auth, league_acc,
                                    new_acc_data):
        """
        PUT /api/games/<game>/{id}/
        Testing PUT update game account details as a normal user.
        """
        response = client.put(league_acc.detail_url,
                              json.dumps(new_acc_data),
                              content_type='application/json',
                              **normal_user_auth)
        assert response.status_code == 200


class TestLeagueOfLegendsAccountViewSet(LeagueOfLegendsSettings, BaseTestAccountViewSet):
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
