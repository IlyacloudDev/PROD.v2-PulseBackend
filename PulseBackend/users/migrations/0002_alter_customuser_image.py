# Generated by Django 5.1.4 on 2025-01-05 08:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='image',
            field=models.ImageField(help_text='Profile picture of the user.', max_length=200, upload_to='avatars/', verbose_name='Profile Image'),
        ),
    ]
