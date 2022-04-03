""" Serializers for the user management """

from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework.validators import UniqueValidator


class ReferrerSerializer(serializers.HyperlinkedModelSerializer):
    """ Serializer for the referrer of the current user """

    class Meta:
        model = get_user_model()
        fields = ("url", "first_name", "last_name")


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

    def update(self, instance, validated_data):
        user = super().update(instance, validated_data)
        return user

    def create(self, validated_data):
        """ Method to create a valid user. """
        user = get_user_model().objects.create_user(**validated_data)

        return user
