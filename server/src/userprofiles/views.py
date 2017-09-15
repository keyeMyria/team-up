from rest_framework import mixins, viewsets

from userprofiles.models import UserProfile
from userprofiles.serializers import UserProfileSerializer


class UserProfileViewSet(mixins.RetrieveModelMixin,
                         mixins.UpdateModelMixin,
                         mixins.ListModelMixin,
                         viewsets.GenericViewSet):
    serializer_class = UserProfileSerializer

    # changed from UserProfile.objects.all() to cancel UnorderedObjectListWarning during tests
    queryset = UserProfile.objects.order_by('id')
