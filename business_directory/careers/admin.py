from cms.admin.placeholderadmin import FrontendEditableAdminMixin
from django.contrib import admin
from .forms import CategoryForm, JobPostAdminForm
from .models import JobPost, Category


class CategoryAdmin(FrontendEditableAdminMixin, admin.ModelAdmin):
    form = CategoryForm
    list_display = ('title', 'slug')


def make_approved(modeladmin, request, queryset):
    queryset.update(approved=True)
make_approved.short_description = "Mark selected posts as approved"


class JobPostAdmin(admin.ModelAdmin):
    form = JobPostAdminForm
    list_display = ('title', 'created_on', 'company', 'status', 'approved')
    actions = [make_approved]


admin.site.register(Category, CategoryAdmin)
admin.site.register(JobPost, JobPostAdmin)
