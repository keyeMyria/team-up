from games.views import LeagueOfLegendsAccountViewSet
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'league', LeagueOfLegendsAccountViewSet, base_name='league_of_legends')

urlpatterns = router.urls
