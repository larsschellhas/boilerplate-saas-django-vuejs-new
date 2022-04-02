from django.contrib.auth import get_user_model
from rest_framework import permissions, viewsets

from usermanagement.serializers import (
    UserSerializer,
)

# Create your views here.


class CurrentUserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """

    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        return (
            get_user_model()
            .objects.all()
            .filter(auth_provider_sub=self.request.user.auth_provider_sub)
            .order_by("id")
        )
