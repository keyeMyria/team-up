import pytest
from oauth2_provider.models import Application

from common.generators import generate_user


@pytest.fixture
def normal_user():
    return generate_user()


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
