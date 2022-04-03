""" Admin setup of usermanagement app

This module contains the setup of the admin dashboard for the models of the usermanagement app.
It registers all custom models.
"""

from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib import admin
from django.utils.translation import gettext_lazy as _

from .models import MyUser


@admin.register(MyUser)
class UserAdmin(BaseUserAdmin):
    """ Admin configuration for the custom user model """

    fieldsets = (
        (None, {"fields": ("email", "password")}),
        (
            _("Personal info"),
            {
                "fields": (
                    "first_name",
                    "last_name",
                    "auth_provider_sub",
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
