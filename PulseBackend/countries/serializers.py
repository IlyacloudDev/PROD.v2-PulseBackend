from rest_framework import serializers
from .models import Country


class CountriesListSerializer(serializers.ModelSerializer):
    """
    Serializer for country objects, providing fields for name, alpha-2 code, alpha-3 code, and region.
    """
    class Meta:
        model = Country
        fields = ['name', 'alpha2', 'alpha3', 'region']
