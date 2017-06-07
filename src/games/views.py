from rest_framework import viewsets, mixins

from games.filters import LeagueFilter
from games.models import LeagueOfLegendsAccount
from games.serializers import LeagueOfLegendsAccountSerializer


class LeagueOfLegendsAccountViewSet(mixins.RetrieveModelMixin,
                                    mixins.UpdateModelMixin,
                                    mixins.ListModelMixin,
                                    mixins.DestroyModelMixin,
                                    viewsets.GenericViewSet):
    serializer_class = LeagueOfLegendsAccountSerializer
    queryset = LeagueOfLegendsAccount.objects.all()
    filter_class = LeagueFilter

