from userprofiles.models import UserProfile

from rest_framework.serializers import (
    HyperlinkedModelSerializer,
)


class UserProfileSerializer(HyperlinkedModelSerializer):

    class Meta:
        model = UserProfile
        exclude = ('user',)
        extra_kwargs = {
            'url': {
                'view_name': 'api-userprofiles:userprofile-detail',
                # 'lookup_field': 'pk'
            },
            'account_league_of_legends': {
                'view_name': 'api-games:league_of_legends-detail',
                # 'lookup_field': 'pk'
            },
        }
