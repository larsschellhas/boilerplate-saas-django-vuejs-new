from djstripe.models.core import Customer, Price
from usermanagement.models import Group, Workspace
from django.contrib.auth import get_user_model
from django_drf_filepond.api import store_upload, delete_stored_upload
from django_drf_filepond.models import StoredUpload, TemporaryUpload
from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password
from djstripe.models import Product, Subscription


class ReferrerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ("url", "first_name", "last_name")


class FilepondSerializer(serializers.ModelSerializer):
    class Meta:
        model = StoredUpload
        fields = ["upload_id"]


class UserSerializer(serializers.HyperlinkedModelSerializer):
    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=get_user_model().objects.all())],
    )
    password = serializers.CharField(
        write_only=True, required=True, validators=[validate_password]
    )
    referrer_email = serializers.EmailField(write_only=True, required=False)
    referrer = ReferrerSerializer(required=False)
    profile_picture_uid = serializers.CharField(
        write_only=True, required=False, max_length=22, min_length=22, allow_null=True
    )
    profile_picture = FilepondSerializer(required=False)

    class Meta:
        model = get_user_model()
        fields = (
            "url",
            "password",
            "email",
            "first_name",
            "last_name",
            "is_staff",
            "initial_setup_done",
            "referrer",
            "referrer_email",
            "terms_and_conditions_accepted",
            "profile_picture",
            "profile_picture_uid",
        )
        extra_kwargs = {
            "is_staff": {"read_only": True},
            "referrer": {"read_only": True},
            "profile_picture": {"read_only": True},
        }

    def validate_terms_and_conditions_accepted(self, value):
        """ Checks whether terms and conditions were accepted. """
        if value:
            return value
        else:
            raise serializers.ValidationError(
                "Terms and conditions must be accepted to create an account."
            )

    def validate(self, attrs):
        """
        Method to check the entered data for user creation.

        It checks first, whether the two provided passwords match. If not, an exception is raised.
        If a referrer email is provided, the referrer is added to the user.
        """

        if "referrer_email" in attrs:
            try:
                attrs["referrer"] = get_user_model().objects.get(
                    email=attrs["referrer_email"]
                )
            except Exception as error:
                raise serializers.ValidationError({"referrer_email": error.message})

        if "profile_picture_uid" in attrs:
            try:
                if attrs["profile_picture_uid"] == None:
                    attrs["profile_picture_temp"] = None
                else:
                    attrs["profile_picture_temp"] = TemporaryUpload.objects.get(
                        upload_id=attrs["profile_picture_uid"]
                    )
            except Exception as error:
                raise serializers.ValidationError(
                    {"profile_picture_uid": "Profile picture upload not found."}
                )

        return attrs

    def create(self, validated_data):
        """ Method to create a valid user. """
        user = get_user_model().objects.create_user(**validated_data)

        return user

    def update(self, instance, validated_data):
        if "password" in validated_data:
            instance.set_password(validated_data.pop("password"))

        if "profile_picture_temp" in validated_data:
            if validated_data["profile_picture_temp"] is not None:
                store_upload(
                    validated_data["profile_picture_uid"],
                    "profilePictures/{0}.{1}".format(
                        validated_data["profile_picture_uid"],
                        validated_data["profile_picture_temp"].upload_name.split(".")[
                            -1
                        ],
                    ),
                )
                validated_data["profile_picture"] = StoredUpload.objects.get(
                    upload_id=validated_data["profile_picture_uid"]
                )
            else:
                validated_data["profile_picture"] = None

            if instance.profile_picture is not None:
                delete_stored_upload(
                    instance.profile_picture.upload_id, delete_file=True
                )

        return super().update(instance, validated_data)


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


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ["url", "name"]


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
