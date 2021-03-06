import pytest
from django.urls import reverse
from django.test import Client

from common.testing import BaseViewTest


class RegularUserProfileSettings:
    view_name = 'api:userprofiles:userprofile'
    # gen_func = staticmethod(generate_league_of_legends_account_data)
    # model = LeagueOfLegendsAccount
    lookup_field = 'pk'
    read_only_fields = ['game_accounts']


class BaseTestUserProfileViewSet(BaseViewTest):
    @pytest.fixture
    def users_auth(self, normal_user_auth, admin_user_auth, normal_user, admin_user):
        """
        Temporary solution... parametrizing with fixtures hasn't been introduced by pytest devs yet.
        It took them 3 years to make a proposal. So my guess would be late 2030...
        https://docs.pytest.org/en/latest/proposals/parametrize_with_fixtures.html
        https://github.com/pytest-dev/pytest/issues/349
        :param normal_user_auth: fixture coming from server/conftest.py
        :param admin_user_auth: fixture coming from server/conftest.py
        :return: dictionary {user_type: auth_headers}
        """
        return {
            'normal': {
                'auth': normal_user_auth,
                'user': normal_user
            },
            'admin': {
                'auth': admin_user_auth,
                'user': admin_user
            },
        }

    @pytest.mark.parametrize('user_type, status_code', [
        ('normal', 200),
        ('admin', 200)
    ])
    def test_can_retrieve_user_profile(self, client: Client, users_auth,
                                       user_type, status_code):
        """
        GET /api/userprofiles/{id}/
        Testing retrieving user profile.
        """
        # that looks like shit thanks to pytest contributors
        # that would look purely amazing if the feature existed
        url = reverse(f'{self.settings_class.view_name}-detail',
                      kwargs={'pk': users_auth[user_type]['user'].userprofile.id})
        response = client.get(url, **users_auth[user_type]['auth'])
        assert response.status_code == status_code

    @pytest.mark.parametrize('user_type, status_code', [
        ('normal', 200),
        ('admin', 200)
    ])
    def test_can_list_user_profiles(self, client: Client, list_url, users_auth,
                                       user_type, status_code):
        response = client.get(list_url, **users_auth[user_type]['auth'])
        assert response.status_code == status_code

    # TODO: test accessing non-existent page as well as existent one GET /api/userprofiles/?page=1


class TestRegularUserProfileViewSet(BaseTestUserProfileViewSet):
    settings_class = RegularUserProfileSettings
