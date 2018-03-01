from django.conf.urls import url

from accounts.views import ValidateUniqueFields

app_name = 'accounts'

urlpatterns = [
    url(r'validate', ValidateUniqueFields.as_view())
]
