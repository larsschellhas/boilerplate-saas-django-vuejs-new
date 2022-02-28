from uuid import uuid4
import django
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)
from django.core.mail import send_mail
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django_drf_filepond.models import StoredUpload
from djstripe.models import Customer, Subscription

if django.VERSION >= (3, 2):
    from django.contrib.auth.hashers import make_password


class UserManager(BaseUserManager):
    """ Inherited UserManager to ensure that created superusers are active. """

    use_in_migrations = True

    def _create_user(self, auth_provider_sub, password=None, **extra_fields):
        """
        Create and save a user with the given email and password.
        """
        if not auth_provider_sub:
            raise ValueError("Auth provider sub has to be provided")
        user = self.model(auth_provider_sub=auth_provider_sub, **extra_fields)

        if password is not None:
            if django.VERSION >= (3, 2):
                user.password = make_password(password)
            else:
                user.set_password(password)

        user.save(using=self._db)
        return user

    def create_user(self, auth_provider_sub, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(auth_provider_sub, password, **extra_fields)

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self._create_user(email, password, **extra_fields)


class AbstractMyUser(AbstractBaseUser, PermissionsMixin):
    """
    An abstract base class implementing a fully featured User model with
    admin-compliant permissions.

    Email and password are required. Other fields are optional.
    """

    auth_provider_sub = models.CharField(
        verbose_name="Auth0 sub identifier",
        max_length=64,
        blank=False,
        unique=True,
    )

    email = models.EmailField(_("email address"), blank=True)
    first_name = models.CharField(_("first name"), max_length=150, blank=True)
    last_name = models.CharField(_("last name"), max_length=150, blank=True)
    is_staff = models.BooleanField(
        _("staff status"),
        default=False,
        help_text=_("Designates whether the user can log into this admin site."),
    )
    is_active = models.BooleanField(
        _("active"),
        default=True,
        help_text=_(
            "Designates whether this user should be treated as active. "
            "Unselect this instead of deleting accounts."
        ),
    )
    date_joined = models.DateTimeField(_("date joined"), default=timezone.now)

    objects = UserManager()

    EMAIL_FIELD = "email"
    USERNAME_FIELD = "auth_provider_sub"

    class Meta:
        verbose_name = _("user")
        verbose_name_plural = _("users")
        abstract = True

    def clean(self):
        super().clean()
        self.email = self.__class__.objects.normalize_email(self.email)

    def get_full_name(self):
        """
        Return the first_name plus the last_name, with a space in between.
        """
        full_name = "%s %s" % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        """Return the short name for the user."""
        return self.first_name

    def email_user(self, subject, message, from_email=None, **kwargs):
        """Send an email to this user."""
        send_mail(subject, message, from_email, [self.email], **kwargs)


class MyUser(AbstractMyUser):
    """
    Users within the Django authentication system are represented by this
    model.
    """

    class Meta(AbstractMyUser.Meta):
        swappable = "AUTH_USER_MODEL"


class Workspace(models.Model):
    """ Company or Workspace that acts as customer and tenant for the user. """

    created_on = models.DateTimeField(verbose_name="Created at", auto_now_add=True)
    workspace_name = models.CharField(
        verbose_name="Workspace name", max_length=100, blank=False
    )

    customer = models.ForeignKey(
        Customer,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        help_text="The workspace's Stripe Customer object, if it exists",
    )
    subscription = models.ForeignKey(
        Subscription,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        help_text="The workspace's Stripe Subscription object, if it exists",
    )

    members = models.ManyToManyField(
        MyUser, verbose_name="Workspace Members", related_name="members"
    )
    admins = models.ManyToManyField(
        MyUser, verbose_name="Workspace Admins", related_name="admins"
    )

    def __str__(self):
        return str(self.workspace_name)

    def add_member(self, user):
        """ Adds a member to a workspace """

        if user not in self.members.all():
            self.members.add(user.id)

    def add_admin(self, user):
        """ Adds an admin to a workspace """

        self.add_member(user)
        if user not in self.admins.all():
            self.admins.add(user.id)

    def remove_admin(self, user):
        """ Removes an admin from a workspace """

        if user in self.admins.all():
            self.admins.remove(user.id)

    def remove_member(self, user):
        """ Removes a member from a workspace """

        self.remove_admin(user)
        if user in self.members.all():
            self.members.remove(user.id)
