from operator import attrgetter

from django.urls import reverse

from common.generators import generate_league_of_legends_account_data, generate_user
from common.testing import auth_headers
from games.models import LeagueOfLegendsAccount


class LeagueOfLegendsSettings:
    view_name = 'api:games:league_of_legends'
    gen_func = staticmethod(generate_league_of_legends_account_data)
    model = LeagueOfLegendsAccount
    lookup_field = 'pk'
    read_only_fields = ['user_profile']


class AccountManager:
    acc_data = {}
    instance = None
    detail_url_var = ''

    user = None
    user_auth = None

    class DetailUrlException(Exception):
        pass

    def _set_user_and_user_auth(self, user_type):
        # needs a little of correction [code]
        if user_type == 'normal':
            generated_user = generate_user()
            start_user = self.normal_user
        elif user_type == 'admin':
            generated_user = generate_user(is_superuser=True)
            start_user = self.admin_user

        if self.user:  # if self.run was used more than once
            self.user = generated_user
        else:
            self.user = start_user

        self.user_auth = auth_headers(self.user)

    def _save_to_db(self):
        self.instance = self.model.objects.create(**self.acc_data)

        # Reasoning in case of LeagueOfLegendsAccount:
        # user_profile was needed to create model instance while not using a request
        # Now it has to be deleted not to hamper further acc_data usage such as sending requests
        # that cannot serialize user_profile instance (it's not needed and doesn't have any
        # impact as user_profile is specified as a read_only field in all GameAccounts serializers
        for field in self.read_only_fields:
            del self.acc_data[field]

        self._set_detail_url()

    def _set_detail_url(self):
        lookup = self.lookup_field.replace('__', '.')
        self.detail_url_var = reverse(f'{self.view_name}-detail', kwargs={
            self.lookup_field: attrgetter(lookup)(self.instance)
        })

    def __init__(self, admin_user, normal_user, settings_class):
        """
        Both admin_user and normal_user are intended to be fixtures passed during
        class initialization.
        """
        self.admin_user = admin_user
        self.normal_user = normal_user

        self.view_name = settings_class.view_name
        self.gen_func = settings_class.gen_func
        self.model = settings_class.model
        self.lookup_field = settings_class.lookup_field
        self.read_only_fields = settings_class.read_only_fields

    def run(self, affiliation, user_type, create=True, user=None):
        """
        This function sets all of these variables: acc_data, instance, detail_url_var, user,
        user_auth. You can specify, if you want to save generated model instance to the database or
        if you want the generated user to be its owner or not.
        :param affiliation: 'own'/'else\'s' whether you want to generated/created object to be
                            yours or not
        :param user_type: 'admin'/'normal' specify type of the generated user
        :param create: boolean whether to save the generated model instance to the database
        :param user: optional argument if you want to specify the owner of the model instance
                    you want to generate/create
        """
        if not user:
            self._set_user_and_user_auth(user_type)
        else:
            self.user = user

        if affiliation == 'own':
            self.acc_data = self.gen_func(self.user)
        elif affiliation == 'else\'s':
            other_user = generate_user()
            # creates and returns another normal type user instance
            # for now running with 'else\'s' argument always creates
            # someone else's model instance with normal type
            self.acc_data = self.gen_func(other_user)

        if create:
            self._save_to_db()

    @property
    def detail_url(self):
        # Is it Pythonic? it looks like wtf
        if self.detail_url_var:
            return self.detail_url_var
        raise self.DetailUrlException(
            "You can't access detail_url without creating account instance.")
