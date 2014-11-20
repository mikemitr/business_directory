# -*- coding: utf-8 -*-
import datetime
import json

from django.conf import settings
from django.core.urlresolvers import reverse, resolve
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.utils.translation import override, get_language_from_request
from django.views import generic
from django.views.generic.dates import ArchiveIndexView
from django.views.generic.detail import DetailView
from django.views.generic.edit import FormMixin
from django.views.generic.list import ListView

from menus.utils import set_language_changer
from aldryn_common.paginator import DiggPaginator, paginate_by

from aldryn_blog.forms import CommentForm
from aldryn_blog import request_post_identifier
from .models import Post, Category, PostComment
from tagging.models import Tag, TaggedItem


class BasePostView(object):

    def get_queryset(self):
        if self.request.user.is_staff:
            manager = Post.objects
        else:
            manager = Post.published

        if getattr(settings, 'ALDRYN_BLOG_SHOW_ALL_LANGUAGES', False):
            return manager

        return manager.filter_by_current_language()

    def render_to_response(self, context, **response_kwargs):
        response_kwargs['current_app'] = resolve(self.request.path).namespace
        return super(BasePostView, self).render_to_response(context, **response_kwargs)


class ArchiveView(BasePostView, ArchiveIndexView):
    date_field = 'publication_start'
    allow_empty = True
    allow_future = True

    def get_queryset(self):
        qs = BasePostView.get_queryset(self)
        if 'day' in self.kwargs:
            qs = qs.filter(publication_start__day=self.kwargs['day'])
        if 'month' in self.kwargs:
            qs = qs.filter(publication_start__month=self.kwargs['month'])
        if 'year' in self.kwargs:
            qs = qs.filter(publication_start__year=self.kwargs['year'])
        return qs

    def get_context_data(self, **kwargs):
        page = self.request.GET.get('page', 1)
        kwargs['day'] = int(self.kwargs.get('day')) if 'day' in self.kwargs else None
        kwargs['month'] = int(self.kwargs.get('month')) if 'month' in self.kwargs else None
        kwargs['year'] = int(self.kwargs.get('year')) if 'year' in self.kwargs else None
        if kwargs['year']:
            kwargs['archive_date'] = datetime.date(
                kwargs['year'], kwargs['month'] or 1, kwargs['day'] or 1)
        kwargs['page'] = DiggPaginator(kwargs['object_list'], paginate_by(), body=6, padding=2).page(page)
        kwargs['object_list'] = kwargs['page'].object_list
        return super(ArchiveView, self).get_context_data(**kwargs)


class CategoryListView(generic.ListView):
    template_name = 'aldryn_blog/category_list.html'

    def get_queryset(self):
        language = get_language_from_request(self.request, check_path=True)
        return Post.published.get_categories(language)


class CategoryPostListView(BasePostView, ListView):

    def get(self, *args, **kwargs):
        self.object = self.get_object()
        response = super(CategoryPostListView, self).get(*args, **kwargs)
        set_language_changer(self.request, self.object.get_absolute_url)
        return response

    def get_object(self):
        return get_object_or_404(Category.objects.language(), slug=self.kwargs['category'])

    def get_queryset(self):
        qs = super(CategoryPostListView, self).get_queryset()
        return qs.filter(category=self.object)


class TagsListView(generic.ListView):
    template_name = 'aldryn_blog/tag_list.html'

    def get_queryset(self):
        return Tag.objects.all()


class TaggedListView(BasePostView, ListView):
    model = TaggedItem

    def get_queryset(self):
        qs = super(TaggedListView, self).get_queryset()
        tag_name = Tag.objects.get(pk=self.kwargs['tag'])
        return qs.filter(tags__contains=tag_name)

    def get_context_data(self, **kwargs):
        context = super(TaggedListView, self).get_context_data(**kwargs)
        context['tagged_entries'] = Tag.objects.get(pk=self.kwargs['tag'])
        return context


def post_language_changer(language):
    with override(language):
        try:
            return reverse('aldryn_blog:latest-posts', )
        except:
            return '/%s/' % language


class PostDetailView(BasePostView, DetailView, FormMixin):
    form_class = CommentForm

    def get(self, request, *args, **kwargs):
        response = super(PostDetailView, self).get(request, *args, **kwargs)
        post = response.context_data.get('post', None)
        if post:
            setattr(request, request_post_identifier, post)
            if post.language:
                set_language_changer(request, post_language_changer)

        return response

    def get_context_data(self, **kwargs):
        context = super(PostDetailView, self).get_context_data(**kwargs)
        context['comments'] = PostComment.objects.filter(entry=context['post'])
        context['form'] = self.get_form(CommentForm)
        return context


def add_comment(request):
    form = CommentForm(request.POST)
    if form.is_valid():
        obj = form.save(commit=False)
        obj.author = request.user
        obj.save()
        resp = {'success': 'ok'}
        comment = {'author': obj.author.email, 'date': obj.created_on.strftime("%b %d, %Y, %H:%M %p"), 'content': obj.content}
        resp['comment'] = comment
    else:
        resp = {'error': 'Invalid comment'}
    return HttpResponse(content=json.dumps(resp), content_type='application/json')