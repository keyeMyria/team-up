from games.models import LeagueOfLegendsAccount

from rest_framework.serializers import (
    HyperlinkedModelSerializer,
    ValidationError,
)


class LeagueOfLegendsAccountSerializer(HyperlinkedModelSerializer):

    class Meta:
        model = LeagueOfLegendsAccount
        fields = '__all__'
        extra_kwargs = {
            'url': {'view_name': 'api-games:league_of_legends-detail', 'lookup_field': 'pk'},
        }

    def validate(self, data):
        username = data.get('username')
        server = data.get('server')
        qs = LeagueOfLegendsAccount.objects.filter(username=username, server=server)
        if qs.exists():
            # solution needed on how to manage multiple accounts creation
            raise ValidationError('The specified account is already in the database.')
        return data
