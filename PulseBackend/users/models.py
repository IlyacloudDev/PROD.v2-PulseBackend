from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.core.validators import RegexValidator, EmailValidator, MinLengthValidator
from django.utils.translation import gettext_lazy as _


class CustomUserManager(BaseUserManager):
    """
    Custom manager for User model.
    """
    def create_user(self, login, password=None, **extra_fields):
        """
        Create and save a regular user.
        """
        user = self.model(login=login, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, login, password=None, **extra_fields):
        """
        Create and save a superuser with elevated privileges.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(login, password, **extra_fields)


class CustomUser(AbstractBaseUser, PermissionsMixin):
    """
    Custom user model with login, email, and additional fields.
    """
    login = models.CharField(
        verbose_name=_("Login"),
        max_length=30,
        unique=True,
        validators=[
            RegexValidator(regex=r"[a-zA-Z0-9-]+", message=_("Login must contain only letters, numbers, or dashes."))
        ],
        help_text=_("Unique identifier for the user.")
    )
    email = models.EmailField(
        verbose_name=_("Email"),
        max_length=50,
        unique=True,
        validators=[EmailValidator(message=_("Enter a valid email address."))],
        help_text=_("User's email address.")
    )
    password = models.CharField(
        verbose_name=_("Password"),
        max_length=100,
        validators=[
            MinLengthValidator(6, message=_("Password must be at least 6 characters long.")),
            RegexValidator(regex=r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d).+$", message=_("Password must include uppercase, lowercase letters, and numbers."))
        ],
        help_text=_("User's password for authentication.")
    )
    is_staff = models.BooleanField(
        verbose_name=_("Staff status"),
        default=False,
        help_text=_("Designates whether the user can log into this admin site.")
    )
    is_superuser = models.BooleanField(
        verbose_name=_("Superuser status"),
        default=False,
        help_text=_("Designates whether the user has all permissions without explicitly assigning them.")
    )
    is_public = models.BooleanField(
        verbose_name=_("Is Public"),
        default=True,
        help_text=_("Whether the user's profile is publicly visible.")
    )
    phone = models.CharField(
        verbose_name=_("Phone"),
        max_length=20,
        validators=[
            RegexValidator(regex=r"^\+\d+$", message=_("Phone number must start with '+' followed by digits."))
        ],
        help_text=_("User's phone number in international format.")
    )
    image = models.ImageField(
        verbose_name=_("Profile Image"),
        max_length=200,
        upload_to='avatars/',
        help_text=_("Profile picture of the user.")
    )
    country_code = models.CharField(
        verbose_name=_("Country Code"),
        max_length=2,
        help_text=_("ISO 3166-1 alpha-2 code of the user's country.")
    )

    objects = CustomUserManager()

    USERNAME_FIELD = "login"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = _("User")
        verbose_name_plural = _("Users")

    def __str__(self):
        """
        Return the user's login as a string representation.
        """
        return self.login

