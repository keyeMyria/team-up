from rest_framework.routers import DefaultRouter

from games.views import LeagueOfLegendsAccountViewSet

app_name = 'games'

router = DefaultRouter()
router.register(r'league', LeagueOfLegendsAccountViewSet, base_name='league_of_legends')

urlpatterns = router.urls
