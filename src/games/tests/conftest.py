import pytest

from django.core.urlresolvers import reverse

from common.generators import generate_league_of_legends_account_data
from games.models import LeagueOfLegendsAccount
import operator


class SingleAccountCreator:
    d = {}
    view_name = ''
    gen_func = None
    model = None
    lookup_field = ''

    def __init__(self):
        acc_data = self.gen_func()
        instance = self.model.objects.create(**acc_data)
        self.d['acc_data'] = acc_data
        self.d['instance'] = instance
        lookup = self.lookup_field.replace('__', '.')
        self.d['detail_url'] = reverse(f'{self.view_name}-detail', kwargs={
            self.lookup_field:
                operator.attrgetter(lookup)(instance)
        })

    @property
    def existing_acc_data(self):
        return self.d['acc_data']

    @property
    def instance(self):
        return self.d['instance']

    @property
    def detail_url(self):
        return self.d['detail_url']


class LeagueAccountCreator(SingleAccountCreator):
    view_name = 'api:games:league_of_legends'
    gen_func = generate_league_of_legends_account_data
    model = LeagueOfLegendsAccount
    lookup_field = 'pk'


@pytest.fixture
def league_acc():
    league_account = LeagueAccountCreator()
    return league_account
