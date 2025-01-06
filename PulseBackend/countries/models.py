from django.db import models
from django.core.validators import RegexValidator
from django.utils.translation import gettext_lazy as _


class Country(models.Model):
    """
    Model representing a country with its details.
    """
    Europe = 'Europe'
    Africa = 'Africa'
    Americas = 'Americas'
    Oceania = 'Oceania'
    Asia = 'Asia'

    REGIONS = [
        (Europe, _('Europe')),
        (Africa, _('Africa')),
        (Americas, _('Americas')),
        (Oceania, _('Oceania')),
        (Asia, _('Asia')),
    ]

    name = models.CharField(
        verbose_name=_("Country Name"),
        max_length=100,
        help_text=_("Full name of the country.")
    )
    alpha2 = models.CharField(
        verbose_name=_("Alpha-2 Code"),
        max_length=2,
        unique=True,
        validators=[
            RegexValidator(regex=r'^[a-zA-Z]{2}$', message=_("Alpha-2 code must be exactly two letters."))
        ],
        help_text=_("ISO 3166-1 alpha-2 code of the country (2 letters).")
    )
    alpha3 = models.CharField(
        verbose_name=_("Alpha-3 Code"),
        max_length=3,
        validators=[
            RegexValidator(regex=r'^[a-zA-Z]{3}$', message=_("Alpha-3 code must be exactly three letters."))
        ],
        help_text=_("ISO 3166-1 alpha-3 code of the country (3 letters).")
    )
    region = models.CharField(
        verbose_name=_("Region"),
        choices=REGIONS,
        default=Europe,
        help_text=_("Region the country belongs to.")
    )

    class Meta:
        verbose_name = _("Country")
        verbose_name_plural = _("Countries")

    def __str__(self):
        """
        Returns the country name and its alpha-2 code.
        """
        return f"{self.name} ({self.alpha2})"
