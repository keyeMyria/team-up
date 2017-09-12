from django_filters import FilterSet, ChoiceFilter

from games.models import LeagueOfLegendsAccount


class LeagueFilter(FilterSet):
    league = ChoiceFilter(choices=LeagueOfLegendsAccount.LEAGUE_CHOICES)
    division = ChoiceFilter(choices=LeagueOfLegendsAccount.DIVISION_CHOICES)
    server = ChoiceFilter(choices=LeagueOfLegendsAccount.SERVER_CHOICES)

    class Meta:
        model = LeagueOfLegendsAccount
        fields = ['league', 'division', 'server']
