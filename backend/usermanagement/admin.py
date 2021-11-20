from django.contrib import admin
from django.contrib.admin.options import ModelAdmin
from django.contrib.auth.admin import GroupAdmin as BaseGroupAdmin
from django.contrib.auth.models import Group as StockGroup
from django_drf_filepond.models import StoredUpload, TemporaryUpload, TemporaryUploadChunked
from cuser.admin import UserAdmin as CUserAdmin
from .models import User, Group, Workspace
from django.utils.translation import gettext_lazy as _


@admin.register(User)
class UserAdmin(CUserAdmin):
    fieldsets = (
        (None, {"fields": ("email", "password")}),
        (_("Personal info"), {"fields": ("first_name", "last_name", "terms_and_conditions_accepted", "profile_picture")}),
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
    list_display = ("email", "first_name", "last_name",
                    "is_staff", "is_active")
    search_fields = ("email", "first_name", "last_name", "referrer__email")
    ordering = ("-is_staff", "-is_active", "email")


admin.site.unregister(StockGroup)


@admin.register(Group)
class GroupAdmin(BaseGroupAdmin):
    pass


@admin.register(Workspace)
class WorkspaceAdmin(ModelAdmin):
    pass


@admin.register(StoredUpload)
class StoredUploadAdmin(ModelAdmin):
    pass


@admin.register(TemporaryUpload)
class TemporaryUploadAdmin(ModelAdmin):
    pass


@admin.register(TemporaryUploadChunked)
class TemporaryUploadChunkedAdmin(ModelAdmin):
    pass
