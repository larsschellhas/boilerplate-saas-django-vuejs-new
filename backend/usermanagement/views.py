from django.contrib.auth import get_user_model
from django.http import HttpResponse
from djstripe.models import Product
from rest_framework import permissions, viewsets
from rest_framework.decorators import api_view

from usermanagement.models import Group, Workspace
from usermanagement.serializers import (
    GroupSerializer,
    ProductSerializer,
    UserSerializer,
    WorkspaceSerializer,
)

# Create your views here.


def public(request):
    """Test view for public access with auth0"""
    return HttpResponse("You don't need to be authenticated to see this")


@api_view(["GET"])
def private(request):
    """Test view for private access with auth0"""
    return HttpResponse("You should not see this message if not authenticated!")


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
            .filter(id=self.request.user.id)
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


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """

    queryset = Group.objects.all().order_by("id")
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]


class ProductViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows products to be viewed or edited.
    """

    queryset = Product.objects.all().order_by("djstripe_id")
    serializer_class = ProductSerializer
    permission_classes = [permissions.AllowAny]
