from rest_framework.routers import DefaultRouter

from userprofiles.views import UserProfileViewSet

app_name = 'userprofiles'

router = DefaultRouter()
router.register(r'', UserProfileViewSet, base_name='userprofile')

urlpatterns = router.urls
