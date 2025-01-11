from rest_framework import serializers
from .services.users_serializers_services import (
    _validation_of_the_country_code_for_existence,
    _create_new_customuser_instance_with_provided_data
)
from .models import CustomUser


class UserRegistrationSerializer(serializers.ModelSerializer):
    """
    Serializer for user registration. Validates input data, handles
    country code validation, and ensures proper user creation with a hashed password.
    """
    class Meta:
        model = CustomUser
        fields = ['login', 'email', 'password', 'country_code', 'is_public', 'phone', 'image']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def validate_country_code(self, value):
        """
        Validate if the provided country code exists in the system.
        """
        return _validation_of_the_country_code_for_existence(value)

    def create(self, validated_data):
        """
        Create a new user instance with the provided validated data and hash the password.
        """
        password = validated_data.pop('password')
        return _create_new_customuser_instance_with_provided_data(password, **validated_data)

