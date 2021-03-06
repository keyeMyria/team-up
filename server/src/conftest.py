import pytest
from oauth2_provider.models import Application

from common.generators import generate_user
from common.utils import create_user_token


@pytest.fixture
def normal_user():
    user = generate_user()
    user.save()
    return user


@pytest.fixture
def token(normal_user):
    return create_user_token(user=normal_user)


@pytest.fixture(autouse=True)
def application(admin_user):
    application = Application.objects.create(
        client_type=Application.CLIENT_CONFIDENTIAL,
        authorization_grant_type=Application.GRANT_AUTHORIZATION_CODE,
        redirect_uris='https://localhost/oauth2/callback',
        name='test',
        user=admin_user
    )
    return application
