from django.contrib.auth import get_user_model
from django.db import models
from django.conf import settings
from cuser.models import AbstractCUser, CUserManager
from cuser.models import Group as CUserGroup
from django.db.models.fields import related
from django_countries.fields import CountryField
from django_drf_filepond.api import store_upload
from django_drf_filepond.models import StoredUpload
from django.utils.translation import gettext_lazy as _
from djmoney.models.fields import MoneyField
from djmoney.models.validators import MinMoneyValidator
from djmoney.money import Money

# Create your models here.


class UserManager(CUserManager):
    """ Inherited UserManager to ensure that created superusers are active. """

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)


class User(AbstractCUser):
    """ This is our custom model for the user management. """

    objects = UserManager()
    is_active = models.BooleanField(
        _("active"),
        default=True,
        help_text=_(
            "Designates whether this user should be treated as active. "
            "Unselect this instead of deleting accounts."
        ),
    )
    initial_setup_done = models.BooleanField(
        _("setup"),
        default=False,
        help_text=_(
            "Designates whether this user has been setup with additional "
            "information after their creation. This can be used for "
            "displaying a 'First Setup' page after login."
        )
    )

    profile_picture = models.ForeignKey(
        StoredUpload,
        verbose_name="Profile picture",
        default=None,
        blank=True,
        null=True,
        on_delete=models.SET_DEFAULT,
    )

    terms_and_conditions_accepted = models.BooleanField(
        _("Terms and Conditions accepted"),
        default=False,
        help_text=_(
            "Designates whether a user accepted the terms and conditions. "
            "Acceptance is required to use any functionality of the app."
        )
    )

    referrer = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        verbose_name="Referrer",
        default=None,
        blank=True,
        null=True,
        on_delete=models.SET_DEFAULT,
    )


class Group(CUserGroup):
    class Meta:
        verbose_name = _("group")
        verbose_name_plural = _("groups")
        proxy = True


class SubscriptionPlan(models.Model):
    """
    Subscription plan which includes features, pricing, and other information
    about a subscription that can be booked through a workspace.
    """

    created_on = models.DateTimeField(
        verbose_name="Created at", auto_now_add=True)
    name = models.CharField(verbose_name="Name", max_length=100, blank=False)
    description = models.CharField(verbose_name="Description", max_length=200)
    price_validators = [
        MinMoneyValidator(0)
    ]
    price_monthly = MoneyField(verbose_name="Price with monthly payment", max_digits=19,
                               decimal_places=2, default_currency="EUR", validators=price_validators, default=Money('10', 'EUR'))
    price_yearly = MoneyField(verbose_name="Price with yearly payment", max_digits=19,
                              decimal_places=2, default_currency="EUR", validators=price_validators, default=Money('10', 'EUR'))
    features = models.JSONField(
        verbose_name="The plan\'s features as a list of dictionaries e.g. [\"This is a feature\", \"This is another feature\"]")
    buttonText = models.CharField(
        verbose_name="Button text", max_length=40, blank=False)

    def __str__(self):
        return '{0} ({1} monthly)'.format(self.name, self.price_monthly)


class Workspace(models.Model):
    """ Company or Workspace that acts as customer and tenant for the user. """

    YEARLY = "Y"
    MONTHLY = "M"
    PAYMENTCYCLECHOICES = [
        (YEARLY, "Yearly"),
        (MONTHLY, "Monthly")
    ]

    created_on = models.DateTimeField(
        verbose_name="Created at", auto_now_add=True)
    workspace_name = models.CharField(
        verbose_name="Workspace name", max_length=100, blank=False)
    company_name = models.CharField(
        verbose_name="Company name", max_length=100, blank=False)
    street = models.CharField(verbose_name="Street",
                              max_length=100, blank=False)
    streetnumber = models.CharField(
        verbose_name="Street number", max_length=10, blank=False)
    postal_code = models.CharField(
        verbose_name="Postal code", max_length=10, blank=False)
    city = models.CharField(verbose_name="City", max_length=100, blank=False)
    state = models.CharField(verbose_name="State", max_length=100, blank=True)
    country = CountryField(verbose_name="Country")

    members = models.ManyToManyField(
        User, verbose_name="Workspace Members", related_name="members")
    admins = models.ManyToManyField(
        User, verbose_name="Workspace Admins", related_name="admins")

    subscriptionPlan = models.ForeignKey(
        SubscriptionPlan,
        verbose_name="Subscription plan",
        default=None,
        blank=True,
        null=True,
        on_delete=models.SET_DEFAULT,
    )

    paymentCycle = models.CharField(
        verbose_name="Payment cycle",
        max_length=1,
        choices=PAYMENTCYCLECHOICES,
        default=YEARLY
    )

    def __str__(self):
        return self.workspace_name

    def add_member(self, user):
        """ Adds a member to a workspace """

        if (user not in self.members.all()):
            self.members.add(user.id)

    def add_admin(self, user):
        """ Adds an admin to a workspace """

        self.add_member(user)
        if (user not in self.admins.all()):
            self.admins.add(user.id)

    def remove_admin(self, user):
        """ Removes an admin from a workspace """

        if (user in self.admins.all()):
            self.admins.remove(user.id)

    def remove_member(self, user):
        """ Removes a member from a workspace """

        self.remove_admin(user)
        if (user in self.members.all()):
            self.members.remove(user.id)
