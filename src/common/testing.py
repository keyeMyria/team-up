from accounts.models import User
from common.utils import create_user_token


def auth_headers(user: User) -> dict:
    token = create_user_token(user=user)
    headers = {
        'Authorization': 'Bearer {}'.format(token)
    }
    return headers
