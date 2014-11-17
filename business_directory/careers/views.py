from .models import Category, JobPost

# view imports
from django.views.generic import DetailView
from django.views.generic import CreateView
from django.views.generic import ListView
from django.core.urlresolvers import reverse_lazy

from braces.views import LoginRequiredMixin, PermissionRequiredMixin


class CategoryDetailView(LoginRequiredMixin, DetailView):
    model = Category

    def get_context_data(self, **kwargs):
        context = super(CategoryDetailView, self).get_context_data(**kwargs)
        job_reverse = dict((v, k) for k, v in JobPost.JOB_STATUS_CHOICES)
        context['jobpost_list'] = JobPost.objects.filter(category=kwargs['object'], status=job_reverse['Open'])
        return context


class CategoryListView(LoginRequiredMixin, ListView):
    model = Category


class JobPostDetailView(LoginRequiredMixin, DetailView):
    model = JobPost


class JobPostListView(LoginRequiredMixin, ListView):
    model = JobPost
    job_reverse = dict((v, k) for k, v in JobPost.JOB_STATUS_CHOICES)
    queryset = JobPost.objects.filter(status=job_reverse['Open'])


class JobPostCreateView(PermissionRequiredMixin, CreateView):
    model = JobPost
    permission_required = 'careers.add_jobpost'
    success_url = reverse_lazy('careers:posts')
    redirect_field_name = 'login'