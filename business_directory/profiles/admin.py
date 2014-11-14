from django.contrib import admin
from .forms import CompanyForm, EmployeeForm
from .models import CompanyProfile, EmployeeProfile


class CompanyProfileAdmin(admin.ModelAdmin):
    form = CompanyForm
    list_display = ('company_name',)


class EmployeeProfileAdmin(admin.ModelAdmin):
    form = EmployeeForm
    list_display = ('last_name', 'first_name')


admin.site.register(CompanyProfile, CompanyProfileAdmin)
admin.site.register(EmployeeProfile, EmployeeProfileAdmin)