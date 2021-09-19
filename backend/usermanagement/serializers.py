from usermanagement.models import Group, Workspace, SubscriptionPlan
from django.contrib.auth import get_user, get_user_model
from django.db.models import fields
from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password


class ReferrerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ("url", "first_name", "last_name")


class UserSerializer(serializers.HyperlinkedModelSerializer):
    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=get_user_model().objects.all())],
    )
    password = serializers.CharField(
        write_only=True, required=True, validators=[validate_password]
    )
    password2 = serializers.CharField(write_only=True, required=True)
    referrer_email = serializers.EmailField(write_only=True, required=False)
    referrer = ReferrerSerializer(required=False)

    class Meta:
        model = get_user_model()
        fields = (
            "url",
            "password",
            "password2",
            "email",
            "first_name",
            "last_name",
            "is_staff",
            "referrer",
            "referrer_email",
        )
        extra_kwargs = {
            "first_name": {"required": True},
            "last_name": {"required": True},
            "is_staff": {"read_only": True},
            "referrer": {"read_only": True},
        }

    def validate(self, attrs):
        """
        Method to check the entered data for user creation.

        It checks first, whether the two provided passwords match. If not, an exception is raised.
        If a referrer email is provided, the referrer is added to the user.
        """

        attrs["is_active"] = True
        attrs["referrer"] = None

        if attrs["password"] != attrs["password2"]:
            raise serializers.ValidationError(
                {"password": "Password fields didn't match."}
            )
        elif attrs["password"] == "":
            attrs["password"] = get_user_model(
            ).objects.make_random_password(length=16)

        if "referrer_email" in attrs:
            attrs["referrer"] = get_user_model().objects.get(
                email=attrs["referrer_email"]
            )
            if attrs["referrer"].is_active == True:
                attrs["is_active"] = True

        return attrs

    def create(self, validated_data):
        """ Method to create a valid user. """
        user = get_user_model().objects.create_user(
            email=validated_data["email"],
            password=validated_data["password"],
            first_name=validated_data["first_name"],
            last_name=validated_data["last_name"],
            referrer=validated_data["referrer"],
            is_active=validated_data["is_active"]
        )

        return user


class WorkspaceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Workspace
        fields = ["url", "workspace_name", "company_name", "street", "streetnumber",
                  "postal_code", "city", "state", "country", "subscriptionPlan", "paymentCycle"]

    def validate(self, attrs):
        """
        Method to check the entered data for user creation.

        It checks first, whether the two provided passwords match. If not, an exception is raised.
        If a referrer email is provided, the referrer is added to the user.
        """

        if attrs["workspace_name"] == "":
            raise serializers.ValidationError(
                {"workspace_name": "Workspace name must not be empty."}
            )
        if attrs["company_name"] == "":
            raise serializers.ValidationError(
                {"company_name": "Company name must not be empty."}
            )
        if attrs["street"] == "":
            raise serializers.ValidationError(
                {"street": "Street must not be empty."}
            )
        if attrs["streetnumber"] == "":
            raise serializers.ValidationError(
                {"streetnumber": "Street number must not be empty."}
            )
        if attrs["postal_code"] == "":
            raise serializers.ValidationError(
                {"postal_code": "Postal code must not be empty."}
            )
        if attrs["city"] == "":
            raise serializers.ValidationError(
                {"city": "City must not be empty."}
            )
        if attrs["country"] == "":
            raise serializers.ValidationError(
                {"country": "Country must not be empty."}
            )
        if attrs["subscriptionPlan"] == "":
            raise serializers.ValidationError(
                {"subscriptionPlan": "Subscription plan must not be empty."}
            )
        if attrs["paymentCycle"] == "":
            raise serializers.ValidationError(
                {"paymentCycle": "Payment cycle must not be empty."}
            )

        return attrs

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


class SubscriptionPlanSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = SubscriptionPlan
        fields = ["url", "name", "description",
                  "price_monthly", "price_monthly_currency", "price_yearly", "price_yearly_currency", "features", "buttonText"]
