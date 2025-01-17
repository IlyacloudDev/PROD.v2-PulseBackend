from rest_framework.generics import ListAPIView, RetrieveAPIView
from .serializers import CountriesListSerializer
from rest_framework.exceptions import ValidationError
from .services.countries_views_services import (
    _validation_of_regions_to_get_countries_by_filtering,
    _get_countries
)


class CountriesListAPIView(ListAPIView):
    """
    Retrieves a list of countries, with optional filtering by regions.
    """
    serializer_class = CountriesListSerializer

    def get_queryset(self):
        """
        Filters the queryset based on the `region` query parameter.
        """
        regions = self.request.query_params.getlist('region', None)
        try:
            return _validation_of_regions_to_get_countries_by_filtering(regions)
        except ValidationError as exc:
            raise ValidationError({"reason": exc.detail})


class CountryDetailAPIView(RetrieveAPIView):
    """
    Filters the queryset based on the `region` query parameter.
    """
    queryset = _get_countries()
    serializer_class = CountriesListSerializer
    lookup_field = 'alpha2'
