from django import forms
from .models import EmployeeProfile, CompanyProfile


class CompanyForm(forms.ModelForm):

    class Meta:
        model=CompanyProfile


class EmployeeForm(forms.ModelForm):

    class Meta:
        model=EmployeeProfile