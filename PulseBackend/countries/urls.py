from django.urls import path
from .views import CountriesListAPIView, CountryDetailAPIView


urlpatterns = [
    path('', CountriesListAPIView.as_view(), name='countries_list'),
    path('<str:alpha2>/', CountryDetailAPIView.as_view(), name='country_detail')
]
