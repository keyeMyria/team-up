from rest_framework import viewsets

from userprofiles.models import UserProfile
from userprofiles.serializers import UserProfileSerializer


class UserProfileViewSet(viewsets.ModelViewSet):
    serializer_class = UserProfileSerializer
    queryset = UserProfile.objects.all()
