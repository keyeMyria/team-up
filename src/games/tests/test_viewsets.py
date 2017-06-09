import json
import pytest

from django.test import Client

from common.testing import BaseViewTest
from games.tests.conftest import LeagueOfLegendsSettings


class BaseTestAccountViewSet(BaseViewTest):
    gen_func = None

    @pytest.mark.parametrize('affiliation, user_type, create, status_code', [
        ('own', 'normal', False, 201),
        ('own', 'admin', False, 201)
    ])
    def test_can_create_account(self, client: Client, mgr, list_url,
                                affiliation, user_type, create, status_code):
        """
        POST /api/games/<game>/
        Testing creating new game account.
        """
        mgr.run(affiliation, user_type, create)
        response = client.post(list_url, mgr.acc_data, **mgr.user_auth)
        assert response.status_code == status_code

    @pytest.mark.parametrize('affiliation, user_type, create, status_code', [
        ('own', 'normal', True, 200),
        ('else\'s', 'normal', True, 200),
        ('own', 'admin', True, 200),
        ('else\'s', 'admin', True, 200),
    ])
    def test_can_retrieve_account(self, client: Client, mgr,
                                  affiliation, user_type, create, status_code):
        """
        GET /api/games/<game>/{id}/
        Testing retrieving game account.
        """
        mgr.run(affiliation, user_type, create)
        response = client.get(mgr.detail_url, **mgr.user_auth)
        assert response.status_code == status_code

    @pytest.mark.parametrize('affiliation, user_type, create, status_code', [
        ('own', 'normal', True, 204),
        ('else\'s', 'normal', True, 403),
        ('own', 'admin', True, 204),
        ('else\'s', 'admin', True, 204),

    ])
    def test_can_delete_account(self, client: Client, mgr,
                                affiliation, user_type, create, status_code):
        """
        DELETE /api/games/<game>/{id}/
        Testing deleting game account.
        """
        mgr.run(affiliation, user_type, create)
        response = client.delete(mgr.detail_url, **mgr.user_auth)
        assert response.status_code == status_code

    @pytest.mark.parametrize('affiliation, user_type, create, status_code', [
        ('own', 'normal', True, 200),
        ('else\'s', 'normal', True, 403),
        ('own', 'admin', True, 200),
        ('else\'s', 'admin', True, 200),

    ])
    @pytest.mark.parametrize('key', [
        'username',
        'league',
        'division',
        'server',
    ])
    def test_can_patch_update_account(self, client: Client, mgr, key,
                                      affiliation, user_type, create, status_code):
        """
        PATCH /api/games/<game>/{id}/
        Testing patch updating game account details.
        Patching with {"user_profile": num} always returns 200 as it is read_only field,
        so there's no reason to test it.
        """
        mgr.run(affiliation, user_type, create)
        data = {key: mgr.acc_data[key]}
        response = client.patch(mgr.detail_url,
                                json.dumps(data),
                                content_type='application/json',
                                **mgr.user_auth)
        assert response.status_code == status_code

    @pytest.mark.parametrize('affiliation, user_type, create, status_code', [
        ('own', 'normal', True, 200),
        ('else\'s', 'normal', True, 403),
        ('own', 'admin', True, 200),
        ('else\'s', 'admin', True, 200),
    ])
    def test_can_put_update_account(self, client: Client, mgr,
                                    affiliation, user_type, create, status_code):
        """
        PUT /api/games/<game>/{id}/
        Testing PUT update game account details.
        """
        # need to find a nice way to generate update acc data!!
        # not sure if needed I guess not
        mgr.run(affiliation, user_type, create)
        response = client.put(mgr.detail_url,
                              json.dumps(mgr.acc_data),
                              content_type='application/json',
                              **mgr.user_auth)
        assert response.status_code == status_code


class TestLeagueOfLegendsAccountViewSet(LeagueOfLegendsSettings, BaseTestAccountViewSet):
    @pytest.mark.parametrize('affiliation, user_type, create, status_code', [
        ('own', 'normal', True, 400),
        ('else\'s', 'normal', True, 400),
        ('own', 'admin', True, 400),
        ('else\'s', 'admin', True, 400),
    ])
    def test_cannot_create_duplicate_account(self, client: Client, mgr, list_url,
                                             affiliation, user_type, create, status_code):
        """
        POST /api/games/league/
        Ensure we cannot create a duplicate of an account.
        """
        mgr.run(affiliation, user_type, create)
        response = client.post(list_url, mgr.acc_data, **mgr.user_auth)
        assert response.status_code == status_code
        error_message = 'The fields username, server must make a unique set.'
        assert error_message in response.data['non_field_errors']
