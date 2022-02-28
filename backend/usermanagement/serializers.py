from djstripe.models.core import Customer, Price
from usermanagement.models import Workspace
from django.contrib.auth import get_user_model
from django_drf_filepond.api import store_upload, delete_stored_upload
from django_drf_filepond.models import StoredUpload
from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from djstripe.models import Product, Subscription


class ReferrerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ("url", "first_name", "last_name")


class FilepondSerializer(serializers.ModelSerializer):
    """ Serializer for the filepond API """

    class Meta:
        model = StoredUpload
        fields = ["upload_id"]


class UserSerializer(serializers.HyperlinkedModelSerializer):
    """ Serializer for the user API """

    url = serializers.HyperlinkedIdentityField(view_name="user-detail")
    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=get_user_model().objects.all())],
    )
    auth_provider_sub = serializers.CharField(
        required=True,
        validators=[UniqueValidator(queryset=get_user_model().objects.all())],
        write_only=True,
    )

    class Meta:
        model = get_user_model()
        fields = (
            "url",
            "email",
            "first_name",
            "last_name",
            "is_staff",
            "auth_provider_sub",
        )
        extra_kwargs = {
            "is_staff": {"read_only": True},
        }

    def validate(self, attrs):
        """
        Method to check the entered data for user creation.

        It checks first, whether the two provided passwords match. If not, an exception is raised.
        If a referrer email is provided, the referrer is added to the user.
        """

        return attrs

    def create(self, validated_data):
        """ Method to create a valid user. """
        user = get_user_model().objects.create_user(**validated_data)

        return user


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer


class SubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscription


class WorkspaceSerializer(serializers.HyperlinkedModelSerializer):
    workspace_name = serializers.CharField(required=True, min_length=4, max_length=120)

    class Meta:
        model = Workspace
        fields = ["url", "workspace_name", "subscription", "customer"]

    def validate_workspace_name(self, value):
        """ Method to check the entered workspace name. """
        if value == "":
            raise serializers.ValidationError("Workspace name must not be empty.")

    def create(self, validated_data):
        """ Method to create a valid workspace. """

        workspace = Workspace(**validated_data)
        workspace.save()

        user = None
        request = self.context.get("request")
        if request and hasattr(request, "user"):
            user = request.user
        workspace.add_admin(user)

        return workspace


class PriceSerialzer(serializers.ModelSerializer):
    class Meta:
        model = Price
        fields = [
            "djstripe_id",
            "id",
            "type",
            "metadata",
            "currency",
            "recurring",
            "unit_amount",
            "unit_amount_decimal",
            "billing_scheme",
        ]


class ProductSerializer(serializers.ModelSerializer):
    prices = PriceSerialzer(instance="get_prices", many=True)

    class Meta:
        model = Product
        fields = [
            "djstripe_id",
            "id",
            "name",
            "type",
            "metadata",
            "description",
            "statement_descriptor",
            "unit_label",
            "prices",
        ]

    def get_prices(self, instance):
        return Price.objects.all().filter(product=instance)
