from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from accounts.models import User


class ValidateUniqueFields(APIView):
    """
    View to check the uniqueness of user fields passed as query params.


    * No authentication is required to access this view.

    """

    permission_classes = (AllowAny,)

    def get(self, request, format=None):
        """
        Check the uniqueness of user fields. Use query parameters to specify filter criteria,
        e.g. ?username=admin&email=admin@sample.com

        If multiple values are associated with one field, take only the first one.

        Returns:
            (Response): Response that wraps a dict of str: str. Each key corresponds to a field,
                value is either 'valid' if the field is unique or 'invalid' otherwise.

        """
        params = dict(self.request.query_params)

        if not params:
            return Response('[BAD REQUEST] No query parameters were specified', status=400)

        response = {}
        for field, values in params.items():
            value = values[0]  # validate only the first value associated with a field
            kwarg = f'{field}__iexact'  # case insensitive

            response[field] = ['valid', 'invalid'][User.objects.filter(**{kwarg: value}).exists()]

        return Response(response)
