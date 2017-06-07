from rest_framework import viewsets, mixins

from userprofiles.models import UserProfile
from userprofiles.serializers import UserProfileSerializer


class UserProfileViewSet(mixins.RetrieveModelMixin,
                         mixins.UpdateModelMixin,
                         mixins.ListModelMixin,
                         mixins.DestroyModelMixin,
                         viewsets.GenericViewSet):
    serializer_class = UserProfileSerializer
    queryset = UserProfile.objects.all()
