import urllib.parse as url_parse

from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.models import AnonymousUser
from chatter.models import TemporaryToken


class OAuthTokenAuthMiddleware:
    """
    Custom middleware that takes Authorization header and read OAuth token from it.
    """

    def __init__(self, inner):
        # Store the ASGI application we were passed
        self.inner = inner

    def __call__(self, scope):
        temp_token = self.get_token(scope)
        scope['user'] = self.validate_token(temp_token)
        return self.inner(scope)

    @staticmethod
    def get_token(scope) -> str:
        return url_parse.parse_qs(scope['query_string'])[b'token'][0].decode("utf-8")

    @staticmethod
    def validate_token(token):
        try:
            token = TemporaryToken.objects.select_related('user').get(token=token)
            if token.is_active():
                token.delete()
                return token.user
            else:
                return AnonymousUser()
        except ObjectDoesNotExist:
            return AnonymousUser()
