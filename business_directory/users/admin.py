# -*- coding: utf-8 -*-
from django.contrib import admin
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from authtools.admin import UserAdmin

from .models import User


class UserAdmin(UserAdmin):
    create_form_class = UserCreationForm
    update_form_class = UserChangeForm


admin.site.register(User, UserAdmin)