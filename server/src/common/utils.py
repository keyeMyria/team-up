import uuid
from datetime import timedelta

from django.utils import timezone
from oauth2_provider.models import AccessToken, Application

from accounts.models import User


def create_user_token(user: User) -> AccessToken:
    app = Application.objects.all()[0]
    access_token, created = AccessToken.objects.get_or_create(
        user=user,
        scope='read write',
        expires=timezone.now() + timedelta(seconds=300),
        token=str(uuid.uuid4()),
        application=app
    )
    return access_token
