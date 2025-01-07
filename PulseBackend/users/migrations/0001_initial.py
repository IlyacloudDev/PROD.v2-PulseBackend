# Generated by Django 5.1.4 on 2025-01-05 08:43

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('login', models.CharField(help_text='Unique identifier for the user.', max_length=30, unique=True, validators=[django.core.validators.RegexValidator(message='Login must contain only letters, numbers, or dashes.', regex='[a-zA-Z0-9-]+')], verbose_name='Login')),
                ('email', models.EmailField(help_text="User's email address.", max_length=50, unique=True, validators=[django.core.validators.EmailValidator(message='Enter a valid email address.')], verbose_name='Email')),
                ('password', models.CharField(help_text="User's password for authentication.", max_length=100, validators=[django.core.validators.MinLengthValidator(6, message='Password must be at least 6 characters long.'), django.core.validators.RegexValidator(message='Password must include uppercase, lowercase letters, and numbers.', regex='^(?=.*[a-z])(?=.*[A-Z])(?=.*\\d).+$')], verbose_name='Password')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='Staff status')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates whether the user has all permissions without explicitly assigning them.', verbose_name='Superuser status')),
                ('is_public', models.BooleanField(default=True, help_text="Whether the user's profile is publicly visible.", verbose_name='Is Public')),
                ('phone', models.CharField(help_text="User's phone number in international format.", max_length=20, validators=[django.core.validators.RegexValidator(message="Phone number must start with '+' followed by digits.", regex='^\\+\\d+$')], verbose_name='Phone')),
                ('image', models.ImageField(blank=True, help_text='Profile picture of the user.', max_length=200, upload_to='avatars/', verbose_name='Profile Image')),
                ('country_code', models.CharField(help_text="ISO 3166-1 alpha-2 code of the user's country.", max_length=2, verbose_name='Country Code')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'User',
                'verbose_name_plural': 'Users',
            },
        ),
    ]