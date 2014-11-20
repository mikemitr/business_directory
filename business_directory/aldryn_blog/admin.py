# -*- coding: utf-8 -*-
from django.contrib import admin

from cms.admin.placeholderadmin import PlaceholderAdmin, FrontendEditableAdmin
from hvad.admin import TranslatableAdmin

from .forms import PostForm, CategoryForm
from .models import Post, Category, PostComment


class PostAdmin(FrontendEditableAdmin, PlaceholderAdmin):

    render_placeholder_language_tabs = False
    list_display = ['title', 'author', 'publication_start', 'publication_end']
    date_hierarchy = 'publication_start'
    form = PostForm
    frontend_editable_fields = ('title', 'lead_in')

    _fieldsets = [
        (None, {
            'fields': ['title', 'slug', 'publication_start', 'publication_end', 'author', 'coauthors', 'language']
        }),
        (None, {
            'fields': ['lead_in', 'category', 'tags']
        }),
        ('Content', {
            'classes': ['plugin-holder', 'plugin-holder-nopage'],
            'fields': ['content']
        }),
    ]

    # def get_fieldsets(self, request, obj=None):
    #     fieldsets = copy.deepcopy(self._fieldsets)
    #     return fieldsets
    #

    # def add_view(self, request, *args, **kwargs):
    #     data = request.GET.copy()
    #     data['author'] = request.user.id  # default author is logged-in user
    #     request.GET = data
    #     return super(PostAdmin, self).add_view(request, *args, **kwargs)

admin.site.register(Post, PostAdmin)


class CategoryAdmin(TranslatableAdmin):

    form = CategoryForm
    list_display = ['__unicode__', 'all_translations', 'ordering']
    list_editable = ['ordering']

    def get_fieldsets(self, request, obj=None):
        fieldsets = [
            (None, {'fields': ['name', 'slug']}),
        ]
        return fieldsets

admin.site.register(Category, CategoryAdmin)


class PostCommentAdmin(admin.ModelAdmin):
    pass

admin.site.register(PostComment, PostCommentAdmin)

