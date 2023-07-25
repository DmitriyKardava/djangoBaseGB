from django.contrib import admin

from authapp import models as authapp_models
from django.utils.translation import gettext_lazy as _


@admin.register(authapp_models.CustomUser) 
class UsersAdmin(admin.ModelAdmin):
    list_display = ["id", "username", "email", "is_active", "date_joined"]
    ordering = ["-date_joined"]
