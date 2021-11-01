from django.apps import AppConfig


class UserManagementConfig(AppConfig):
    name = "usermanagement"
    verbose_name = "User Management & Authentication"

    def ready(self):

        # Import configuration for password-reset emails
        import usermanagement.signals
