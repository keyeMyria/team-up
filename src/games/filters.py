from django_filters import FilterSet, ChoiceFilter
from django.utils.text import ugettext_lazy as _

from games.models import LeagueOfLegendsAccount


# temporary duplication!!!!!!
LEAGUE_CHOICES = (
    (1, _('Bronze')),
    (2, _('Silver')),
    (3, _('Gold')),
    (4, _('Platinum')),
    (5, _('Diamond')),
    (6, _('Master')),
    (7, _('Challenger'))
)
DIVISION_CHOICES = (
    (1, 'I'),
    (2, 'II'),
    (3, 'III'),
    (4, 'IV'),
    (5, 'V'),
)
SERVER_CHOICES = (
    (1, _('North America')),
    (2, _('EU West')),
    (3, _('EU Nordic & East')),
    (4, _('Latin America North')),
    (5, _('Latin America South')),
    (6, _('Brazil')),
    (7, _('Turkey')),
    (8, _('Russia')),
    (9, _('Oceania')),
    (10, _('Japan')),
    (11, _('Korea')),
)


class LeagueFilter(FilterSet):
    league = ChoiceFilter(choices=LEAGUE_CHOICES)
    division = ChoiceFilter(choices=DIVISION_CHOICES)
    server = ChoiceFilter(choices=SERVER_CHOICES)

    class Meta:
        model = LeagueOfLegendsAccount
        fields = ['league', 'division', 'server']
