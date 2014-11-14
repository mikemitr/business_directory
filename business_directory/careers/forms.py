from django import forms
from .models import Category, JobPost


class CategoryForm(forms.ModelForm):

    class Meta:
        model = Category


class JobPostForm(forms.ModelForm):

    class Meta:
        model = JobPost