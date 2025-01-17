from rest_framework import serializers
from .services.users_serializers_services import (
    _validation_of_the_country_code_for_existence,
    _create_new_customuser_instance_with_provided_data,
    _validation_the_old_password_when_changing_it,
    _validation_a_new_password_when_setting_it,
    _set_a_new_password,
    _validation_provided_login_to_get_user
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


class UserProfileSerializer(serializers.ModelSerializer):
    """
    Serializer for retrieving and updating the user profile.
    """
    class Meta:
        model = CustomUser
        fields = ['login', 'email', 'country_code', 'is_public', 'phone', 'image']
        extra_kwargs = {
            'login': {'read_only': True},
            'email': {'read_only': True}
        }

    def validate_country_code(self, value):
        """
        Validate if the provided country code exists in the system.
        """
        return _validation_of_the_country_code_for_existence(value)


class UserUpdatePasswordSerializer(serializers.ModelSerializer):
    """
    Serializer for updating the user's password.
    Requires old and new passwords.
    """
    old_password = serializers.CharField(write_only=True, required=True)
    new_password = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = CustomUser
        fields = ['old_password', 'new_password']

    def validate_old_password(self, value):
        """
        Validate that the provided old password matches the current user's password.
        """
        user = self.instance
        return _validation_the_old_password_when_changing_it(value, user)

    def validate_new_password(self, value):
        """
        Validate the new password using Django's password validation framework.
        """
        user = self.instance
        return _validation_a_new_password_when_setting_it(value, user)

    def update(self, instance, validated_data):
        """
        Update the user's password.
        """
        password = validated_data['new_password']
        user = instance
        return _set_a_new_password(password, user)


class UserFriendAddRemoveSerializer(serializers.Serializer):
    """
    Serializer for adding or removing a user from the friends list.
    """
    login = serializers.CharField(required=True)

    def validate_login(self, value):
        """
        Validate that the user exists with the provided login.
        """
        target_user = _validation_provided_login_to_get_user(value)
        self.context['target_user'] = target_user
        return value

    def create(self, validated_data):
        """
        Perform the add or remove action based on the view's context.
        """
        user = self.context['request'].user
        target_user = self.context.get('target_user')
        action = self.context.get('action')

        if target_user and target_user != user:
            if action == 'add':
                user.friends.add(target_user)
            elif action == 'remove':
                user.friends.remove(target_user)

        return user
