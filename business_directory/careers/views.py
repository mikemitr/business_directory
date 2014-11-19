from profiles.models import EmployeeProfile
from django.http.response import HttpResponse
from django.shortcuts import get_object_or_404, redirect
from .models import Category, JobPost, JobPostApplied
from .forms import JobPostAppliedForm, JobPostForm
# view imports
from django.views.generic import DetailView
from django.views.generic import CreateView
from django.views.generic import ListView
from django.core.urlresolvers import reverse_lazy
from django.views.generic.edit import FormMixin

from braces.views import LoginRequiredMixin, PermissionRequiredMixin
from .utils import send_apply_messsage
import json


class CategoryDetailView(LoginRequiredMixin, DetailView):
    model = Category

    def get_context_data(self, **kwargs):
        context = super(CategoryDetailView, self).get_context_data(**kwargs)
        job_reverse = dict((v, k) for k, v in JobPost.JOB_STATUS_CHOICES)
        context['jobpost_list'] = JobPost.objects.filter(category=kwargs['object'], status=job_reverse['Open'])
        return context


class CategoryListView(LoginRequiredMixin, ListView):
    model = Category
    paginate_by = 20


class JobPostDetailView(LoginRequiredMixin, FormMixin, DetailView):
    model = JobPost
    form_class = JobPostAppliedForm
    template_name = 'careers/jobpost_detail.html'

    def get_context_data(self, **kwargs):
        context = super(JobPostDetailView, self).get_context_data(**kwargs)
        context['form'] = self.form_class(initial=self.initial)
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = JobPostAppliedForm(request.POST, request.FILES)
        response_data = {}

        if form.is_valid():
            jobpost_id = request.path.split('/jobpost/')[-1].replace('/', '')
            jobpost = JobPost.objects.get(pk=jobpost_id)

            if not JobPostApplied.objects.filter(jobpost=jobpost, applicant=self.request.user).exists():
                message = form.cleaned_data['message']
                msg = send_apply_messsage(jobpost.company.user, message, request.user)

                application = JobPostApplied()
                application.jobpost = jobpost
                application.message = msg
                application.resume = request.FILES.get('resume', '')
                application.applicant = request.user
                application.save()
                response_data['notification'] = 'You have successfully applied a job!'
            else:
                response_data['warning'] = 'You have already applied to this job post'
            return HttpResponse(json.dumps(response_data), content_type='application/json')
        else:
            response_data['error'] = form.errors
            return HttpResponse(json.dumps(response_data), content_type='application/json')


class JobPostListView(LoginRequiredMixin, ListView):
    model = JobPost
    job_reverse = dict((v, k) for k, v in JobPost.JOB_STATUS_CHOICES)
    queryset = JobPost.objects.filter(status=job_reverse['Open'], approved=True)
    paginate_by = 20


class JobPostCreateView(PermissionRequiredMixin, CreateView):
    model = JobPost
    form_class = JobPostForm
    permission_required = 'careers.add_jobpost'
    success_url = reverse_lazy('careers:posts')
    redirect_field_name = 'login'


class JobPostAppliedListView(LoginRequiredMixin, ListView):
    model = JobPostApplied
    paginate_by = 5

    def get_queryset(self):
        return JobPostApplied.objects.filter(
            jobpost=(JobPost.objects.filter(company=self.request.user)))\
            .order_by('-date')

    def dispatch(self, request, *args, **kwargs):
        if not hasattr(request.user, "company"):
            return redirect("account_login")
        return super(JobPostAppliedListView, self).dispatch(request, args, kwargs)


class JobPostAppliedDetailView(LoginRequiredMixin, DetailView):
    model = JobPostApplied

    def get_context_data(self, **kwargs):
        context = super(JobPostAppliedDetailView, self).get_context_data(**kwargs)
        context['employee'] = get_object_or_404(EmployeeProfile.objects,
            user=context['jobpostapplied'].applicant)
        return context