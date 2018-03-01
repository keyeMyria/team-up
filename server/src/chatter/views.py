from rest_framework.views import APIView
from rest_framework.response import Response

from chatter.models import TemporaryToken


class TemporaryTokenView(APIView):

    def get(self):
        token = TemporaryToken.generate(self.request.user)

        token.save()

        return Response(token.token)
