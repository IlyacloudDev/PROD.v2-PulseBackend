from countries.models import Country
from users.models import CustomUser
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


def _validation_of_the_country_code_for_existence(value):
    """
    Validate whether the provided country code exists in the database.
    """
    countries_alpha2 = Country.objects.all().values_list('alpha2')
    if not (value.upper(),) in countries_alpha2:
        raise ValidationError(_('Country code not found'))
    return value.upper()


def _create_new_customuser_instance_with_provided_data(password, **validated_data):
    """
    Create and save a new CustomUser instance with the provided data and hashed password.
    """
    user = CustomUser(**validated_data)
    user.set_password(password)
    user.save()
    return user
