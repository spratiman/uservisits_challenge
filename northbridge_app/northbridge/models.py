import os

from binascii import hexlify
from django.core import validators
from django.db import models
from django.utils.translation import gettext_lazy as _


class User(models.Model):
    """
    Users onboarded to the Northbridge website
    """

    name = models.CharField(
        max_length=30,
        help_text=_(
            "Required. Between 2 and 30 characters."
            "Cannot start or end with a space."
            "No special symbols outside of accented letters."
        ),
        validators=[
            validators.RegexValidator(
                r"^\w[\w ]*\w+$",
                _(
                    "Enter a valid name. At least 2 characters, "
                    "cannot start or end with a space."
                    "No special symbols outside of accented letters."
                ),
                "invalid",
            )
        ],
    )
    email = models.EmailField(unique=True)
    is_active = models.BooleanField(default=True)


def _create_hash_id():
    """
    Generates a 10 character long hash
    """
    return hexlify(os.random(10))


class Policy(models.Model):
    """
    Northbridge Policy related to each user
    """

    PENDING_POLICY = "P"
    ACTIVE_POLICY = "A"
    EXPIRED_POLICY = "E"

    POLICY_CHOICES = (
        (PENDING_POLICY, "Pending"),
        (ACTIVE_POLICY, "Active"),
        (EXPIRED_POLICY, "Expired")
    )

    user = models.OneToOneField(
        to=User,
        on_delete=models.DO_NOTHING,
        related_name="user_policy",
        blank=False,
        null=False
    )
    hash_id = models.CharField(
        max_length=10, default=_create_hash_id, unique=True)
    start_date = models.DateTimeField()
    state = models.CharField(
        choices=POLICY_CHOICES,
        default=PENDING_POLICY,
        max_length=1,
    )


class Page(models.Model):
    """
    List of Northbridge Website page names
    """

    name = models.CharField(
        max_length=20, unique=True
    )
