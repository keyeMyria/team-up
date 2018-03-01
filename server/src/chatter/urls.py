from rest_framework.routers import DefaultRouter

from chatter.views import TemporaryTokenView

app_name = 'games'

router = DefaultRouter()
router.register(r'temporary-token', TemporaryTokenView, base_name='temporary_ws_token')

urlpatterns = router.urls
