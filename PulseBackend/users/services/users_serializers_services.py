from django.contrib.auth import password_validation
from django.contrib.auth.hashers import check_password
from countries.models import Country
from users.models import CustomUser
from rest_framework.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


def _validation_of_the_country_code_for_existence(value):
    """
    Validate whether the provided country code exists in the database.
    """
    if not Country.objects.filter(alpha2=value.upper()).exists():
        raise ValidationError(_("Country code not found."))
    return value.upper()


def _create_new_customuser_instance_with_provided_data(password, **validated_data):
    """
    Create and save a new CustomUser instance with the provided data and hashed password.
    """
    user = CustomUser(**validated_data)
    user.set_password(password)
    user.save()
    return user


def _validation_the_old_password_when_changing_it(password, user):
    """
    Check if the old password is correct.
    """
    if not check_password(password, user.password):
        raise ValidationError(_("The old password is incorrect."))
    return password


def _validation_a_new_password_when_setting_it(password, user):
    """
    Validate the new password.
    """
    password_validation.validate_password(password, user)
    return password


def _set_a_new_password(password, user):
    """
    Set and save the new password.
    """
    user.set_password(password)
    user.save()
    return user


def _validation_provided_login_to_get_user(value):
    """
    Validate that the user exists with the provided login.
    """
    target_user = CustomUser.objects.filter(login=value)
    if not target_user:
        raise ValidationError(_("User with this login does not exist."))
    return CustomUser.objects.get(login=value)
