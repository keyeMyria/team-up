from django.conf.urls import url
from rest_framework.routers import DefaultRouter

from accounts.views import ValidateUniqueFields, UserViewSet, ChangePassword

app_name = 'accounts'

router = DefaultRouter()
router.register(r'', UserViewSet, base_name='users')

urlpatterns = [
    url(r'validate', ValidateUniqueFields.as_view()),
    url(r'change-password', ChangePassword.as_view())
]

urlpatterns += router.urls
