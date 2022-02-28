from django.contrib.auth import get_user_model
from djstripe.models import Product
from rest_framework import permissions, viewsets

from usermanagement.models import Workspace
from usermanagement.serializers import (
    ProductSerializer,
    UserSerializer,
    WorkspaceSerializer,
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


class WorkspaceViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows workspaces to be viewed or edited.
    """

    Workspace.objects.all()
    serializer_class = WorkspaceSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Workspace.objects.filter(members=self.request.user.id).order_by("id")


class ProductViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows products to be viewed or edited.
    """

    queryset = Product.objects.all().order_by("djstripe_id")
    serializer_class = ProductSerializer
    permission_classes = [permissions.AllowAny]
