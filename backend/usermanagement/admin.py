""" Admin setup of usermanagement app

This module contains the setup of the admin dashboard for the models of the usermanagement app.
It registers all custom models as well as django-drf-filepond's models.
"""

from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib import admin
from django.contrib.admin.options import ModelAdmin
from django.utils.translation import gettext_lazy as _
from django_drf_filepond.models import (
    StoredUpload,
    TemporaryUpload,
    TemporaryUploadChunked,
)

from .models import MyUser


@admin.register(MyUser)
class UserAdmin(BaseUserAdmin):

    fieldsets = (
        (None, {"fields": ("email", "password")}),
        (
            _("Personal info"),
            {
                "fields": (
                    "first_name",
                    "last_name",
                    "auth_provider_sub",
                    "stripe_customer",
                )
            },
        ),
        (
            _("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                )
            },
        ),
        (_("Important dates"), {"fields": ("last_login", "date_joined")}),
    )
    list_display = ("email", "first_name", "last_name", "is_staff", "is_active")
    search_fields = ("email", "first_name", "last_name")
    ordering = ("-is_staff", "-is_active", "email")


@admin.register(StoredUpload)
class StoredUploadAdmin(ModelAdmin):
    """ Admin config for model django_drf_filepond.StoredUpload """


@admin.register(TemporaryUpload)
class TemporaryUploadAdmin(ModelAdmin):
    """ Admin config for model django_drf_filepond.TemporaryUpload """


@admin.register(TemporaryUploadChunked)
class TemporaryUploadChunkedAdmin(ModelAdmin):
    """ Admin config for model django_drf_filepond.TemporaryChunkedUpload """
