from django.contrib.auth import get_user_model
from django_drf_filepond.models import StoredUpload
from djstripe.models import Product, Subscription
from djstripe.models.core import Customer, Price
from rest_framework import serializers
from rest_framework.validators import UniqueValidator


class ReferrerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ("url", "first_name", "last_name")


class FilepondSerializer(serializers.ModelSerializer):
    """ Serializer for the filepond API """

    class Meta:
        model = StoredUpload
        fields = ["upload_id"]


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = (
            "id",
            "address",
            "balance",
            "currency",
            "default_source",
            "delinquent",
            "coupon",
            "coupon_start",
            "coupon_end",
            "email",
            "invoice_prefix",
            "invoice_settings",
            "default_payment_method",
            "name",
            "phone",
            "preferred_locales",
            "shipping",
            "tax_exempt",
            "date_purged",
        )


class SubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscription


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
    stripe_customer = CustomerSerializer()

    class Meta:
        model = get_user_model()
        fields = (
            "url",
            "email",
            "first_name",
            "last_name",
            "is_staff",
            "auth_provider_sub",
            "stripe_customer",
        )
        extra_kwargs = {
            "is_staff": {"read_only": True},
            "stripe_customer": {"read_only": True},
        }

    def update(self, instance, validated_data):
        user = super().update(instance, validated_data)
        if (user.email != "") and (user.stripe_customer is None):
            user.stripe_customer = Customer.get_or_create(subscriber=user)[0]
        return user

    def create(self, validated_data):
        """ Method to create a valid user. """
        user = get_user_model().objects.create_user(**validated_data)

        return user


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
