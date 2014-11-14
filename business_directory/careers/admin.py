from cms.admin.placeholderadmin import FrontendEditableAdminMixin
from django.contrib import admin
from .forms import CategoryForm, JobPostForm
from .models import JobPost, Category


class CategoryAdmin(FrontendEditableAdminMixin, admin.ModelAdmin):
    form = CategoryForm
    list_display = ('title', 'slug')


class JobPostAdmin(admin.ModelAdmin):
    form = JobPostForm
    list_display = ('title', 'created_on', 'company', 'status')


admin.site.register(Category, CategoryAdmin)
admin.site.register(JobPost, JobPostAdmin)
