from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth import get_user_model
from .models import Profile


class ProfileAdmin(admin.ModelAdmin):
    list_display = ['username']


admin.site.register(Profile, ProfileAdmin)
