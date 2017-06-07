import pytest

from common.generators import generate_user


@pytest.fixture
def normal_user():
    return generate_user()


@pytest.fixture
def admin_user():
    return generate_user(is_superuser=True)
