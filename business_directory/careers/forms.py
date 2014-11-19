from django import forms
from django.forms import Textarea
from django.forms.widgets import TextInput
from .models import Category, JobPost, JobPostApplied


class CategoryForm(forms.ModelForm):

    class Meta:
        model = Category


class JobPostForm(forms.ModelForm):

    class Meta:
        model = JobPost
        fields = ['title', 'description', 'company', 'location', 'budget_from',
                  'budget_to', 'status', 'type', 'category']

class JobPostAdminForm(forms.ModelForm):

    class Meta:
        model = JobPost


class JobPostAppliedForm(forms.Form):
    message = forms.CharField()
    resume = forms.FileField(required=False)

    def clean_resume(self):
        file = self.cleaned_data['resume']
        if file:
            ftype = file.content_type
            if ftype == 'application/pdf':
                return file
            else:
                raise forms.ValidationError('File must be a PDF document')
