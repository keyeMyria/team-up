from userprofiles.views import UserProfileViewSet
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'', UserProfileViewSet, base_name='userprofile')

urlpatterns = router.urls
