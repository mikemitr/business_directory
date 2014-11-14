# -*- coding: utf-8 -*-
from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Permission
from django.utils.translation import ugettext_lazy as _
from profiles.models import EmployeeProfile, CompanyProfile

User = get_user_model()


class UserForm(forms.ModelForm):
    class Meta:
        # Set this form to use the User model.
        model = User

        # Constrain the UserForm to just these fields.
        fields = ("email", "password")


class CustomSignupForm(forms.Form):
    """Custom signup form with fields for different user profiles"""
    email = forms.EmailField(widget=forms.TextInput(
        attrs={'type': 'email',
               'placeholder': _('E-mail address')}))

    is_company = forms.BooleanField(label=_('Management company'), required=False)
    company_name = forms.CharField(label=_('Company name'), max_length=255, required=False,
                                   widget=forms.TextInput(
                                       attrs={'placeholder': _('Company name')
                                       }))
    first_name = forms.CharField(label=_('First name'), max_length=100, required=False,
                                 widget=forms.TextInput(
                                     attrs={'placeholder': _('First name')
                                     }))
    last_name = forms.CharField(label=_('Last name'), max_length=100, required=False,
                                widget=forms.TextInput(
                                    attrs={'placeholder': _('Last name')
                                    }))

    def clean(self):
        is_company = self.cleaned_data["is_company"]
        if is_company:
            company = self.cleaned_data["company_name"]
            if not company:
                raise forms.ValidationError("Company name "
                                            "shouldn't be empty.")
        else:
            first = self.cleaned_data["first_name"]
            last = self.cleaned_data["last_name"]
            if not first and not last:
                raise forms.ValidationError("First name and last name "
                                            "shouldn't be empty.")
        return self.cleaned_data

    def clean_email(self):
        email = self.cleaned_data["email"]
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("User with this email is already "
                                        "exist")

    def signup(self, request, user):
        if self.cleaned_data["is_company"]:
            profile = CompanyProfile()
            profile.company_name = self.cleaned_data["company_name"]

            permission = Permission.objects.get(codename='add_jobpost')
            user.user_permissions.add(permission)
        else:
            profile = EmployeeProfile
            profile.first_name = self.cleaned_data["first_name"]
            profile.last_name = self.cleaned_data["last_name"]

        profile.user = user
        profile.save()
        return profile