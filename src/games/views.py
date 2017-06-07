from rest_framework import viewsets

from games.filters import LeagueFilter
from games.models import LeagueOfLegendsAccount
from games.serializers import LeagueOfLegendsAccountSerializer


class LeagueOfLegendsAccountViewSet(viewsets.ModelViewSet):
    serializer_class = LeagueOfLegendsAccountSerializer
    queryset = LeagueOfLegendsAccount.objects.all()
    filter_class = LeagueFilter

