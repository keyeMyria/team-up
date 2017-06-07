from games.models import LeagueOfLegendsAccount

from rest_framework.serializers import HyperlinkedModelSerializer


class LeagueOfLegendsAccountSerializer(HyperlinkedModelSerializer):

    class Meta:
        model = LeagueOfLegendsAccount
        fields = '__all__'
        extra_kwargs = {
            'url': {
                'view_name': 'api:games:league_of_legends-detail',
                'lookup_field': 'pk'
            },
        }
