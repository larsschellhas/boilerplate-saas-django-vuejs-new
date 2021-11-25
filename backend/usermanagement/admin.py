""" Admin setup of usermanagement app

This module contains the setup of the admin dashboard for the models of the usermanagement app.
It registers all custom models as well as django-drf-filepond's models.
"""

from cuser.admin import UserAdmin as CUserAdmin
from django.contrib import admin
from django.contrib.admin.options import ModelAdmin
from django.contrib.auth.admin import GroupAdmin as BaseGroupAdmin
from django.contrib.auth.models import Group as StockGroup
from django.utils.translation import gettext_lazy as _
from django_drf_filepond.models import (
    StoredUpload,
    TemporaryUpload,
    TemporaryUploadChunked,
)

from .models import Group, User, Workspace


@admin.register(User)
class UserAdmin(CUserAdmin):

    fieldsets = (
        (None, {"fields": ("email", "password")}),
        (
            _("Personal info"),
            {
                "fields": (
                    "first_name",
                    "last_name",
                    "terms_and_conditions_accepted",
                    "profile_picture",
                )
            },
        ),
        (_("Referrer"), {"fields": ("referrer",)}),
        (
            _("Permissions"),
            {
                "fields": (
                    "initial_setup_done",
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
    search_fields = ("email", "first_name", "last_name", "referrer__email")
    ordering = ("-is_staff", "-is_active", "email")


admin.site.unregister(StockGroup)


@admin.register(Group)
class GroupAdmin(BaseGroupAdmin):
    """ Admin config for model usermanagement.Group """


@admin.register(Workspace)
class WorkspaceAdmin(ModelAdmin):
    """ Admin config for model usermanagement.Workspace """


@admin.register(StoredUpload)
class StoredUploadAdmin(ModelAdmin):
    """ Admin config for model django_drf_filepond.StoredUpload """


@admin.register(TemporaryUpload)
class TemporaryUploadAdmin(ModelAdmin):
    """ Admin config for model django_drf_filepond.TemporaryUpload """


@admin.register(TemporaryUploadChunked)
class TemporaryUploadChunkedAdmin(ModelAdmin):
    """ Admin config for model django_drf_filepond.TemporaryChunkedUpload """
