from rest_framework.exceptions import ValidationError
from countries.models import Country
from django.utils.translation import gettext_lazy as _


def _validation_of_regions_to_get_countries_by_filtering(regions):
    """
    Validates the list of regions and filters countries based on the provided regions.
    Raises ValidationError if invalid regions are provided.
    """
    if regions:
        valid_regions = Country.objects.values_list('region', flat=True).distinct()
        invalid_regions = [region for region in regions if region not in valid_regions]

        if invalid_regions:
            raise ValidationError(_(f"Invalid regions provided: {', '.join(invalid_regions)}"))

        return Country.objects.filter(region__in=regions).order_by('alpha2')

    return Country.objects.all().order_by('alpha2')


def _get_countries():
    """
    Returns a queryset of all countries, ordered by their alpha-2 code.
    """
    return Country.objects.all().order_by('alpha2')
