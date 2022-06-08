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
