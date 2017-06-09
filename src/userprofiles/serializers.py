from rest_framework.serializers import HyperlinkedModelSerializer, SerializerMethodField, IntegerField

from games.serializers import LeagueOfLegendsAccountSerializer
from userprofiles.models import UserProfile


class UserProfileSerializer(HyperlinkedModelSerializer):
    user = SerializerMethodField()
    game_accounts = SerializerMethodField()

    class Meta:
        model = UserProfile
        fields = '__all__'
        extra_kwargs = {
            'url': {
                'view_name': 'api:userprofiles:userprofile-detail',
                # 'lookup_field': 'pk'
            },
            'account_league_of_legends': {
                'view_name': 'api:games:league_of_legends-detail',
                # 'lookup_field': 'pk'
            },
        }
        read_only_fields = (
            'game_accounts',
        )

    def get_game_accounts(self, user_profile):
        # got other idea? contribute...
        serializers = {
            'LeagueOfLegendsAccount': LeagueOfLegendsAccountSerializer,
        }
        game_accounts = {}
        for acc_type, queryset in user_profile.accounts.items():
            # key = re.sub(r"(\w)([A-Z])", r"\1 \2", acc_type.replace('Account', ''))
            game_accounts[acc_type] = serializers[acc_type](
                queryset,
                many=True,
                context=self.context
            ).data
        return game_accounts

    @staticmethod
    def get_user(user_profile):
        return str(user_profile.user)
