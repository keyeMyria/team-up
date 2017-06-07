from rest_framework import viewsets, mixins

from games.filters import LeagueFilter
from games.models import LeagueOfLegendsAccount
from games.serializers import LeagueOfLegendsAccountSerializer


class LeagueOfLegendsAccountViewSet(mixins.CreateModelMixin,
                                    mixins.RetrieveModelMixin,
                                    mixins.UpdateModelMixin,
                                    mixins.DestroyModelMixin,
                                    mixins.ListModelMixin,
                                    viewsets.GenericViewSet):
    serializer_class = LeagueOfLegendsAccountSerializer
    # pytest having its own problems probably bcs of that:
    # https://github.com/encode/django-rest-framework/issues/5048
    queryset = LeagueOfLegendsAccount.objects.order_by('id')
    filter_class = LeagueFilter

