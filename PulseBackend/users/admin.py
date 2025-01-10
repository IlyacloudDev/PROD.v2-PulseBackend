from django.contrib import admin
from .models import CustomUser


@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    """
    Admin configuration for managing CustomUser instances.
    """
    list_display = ('login', 'phone')
    search_fields = ('login', 'phone')
