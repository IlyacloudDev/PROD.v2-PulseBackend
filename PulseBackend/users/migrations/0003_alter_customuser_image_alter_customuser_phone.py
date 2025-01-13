# Generated by Django 5.1.4 on 2025-01-12 00:31

import django.core.validators
import phonenumber_field.modelfields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_customuser_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='image',
            field=models.URLField(help_text='URL of the profile picture.', validators=[django.core.validators.MinLengthValidator(1)], verbose_name='Profile Image URL'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='phone',
            field=phonenumber_field.modelfields.PhoneNumberField(help_text="User's phone number in international format.", max_length=20, region=None, verbose_name='Phone'),
        ),
    ]
