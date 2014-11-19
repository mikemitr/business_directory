from profiles.models import CompanyProfile
from django.db import models
from django.utils.translation import ugettext_lazy as _
from cms.models import CMSPlugin
from django.core.files.storage import FileSystemStorage
from django.conf import settings
import datetime


fs = FileSystemStorage(location=settings.RESUME_ROOT)


class Category(models.Model):
    title = models.CharField(verbose_name=_('Title'), max_length=100, blank=False)
    slug = models.SlugField(verbose_name=_('Slug'), blank=False, null=False, unique=True)

    class Meta:
        verbose_name = _('Category')
        verbose_name_plural = _('Categories')

    def __unicode__(self):
        return self.title


class JobPost(models.Model):
    title = models.CharField(verbose_name=_('Title'), max_length=100, blank=False)
    description = models.TextField(_('Description'), blank=False)
    created_on = models.DateTimeField(_('Created on'), editable=False, auto_now_add=True)
    company = models.ForeignKey(CompanyProfile)
    location = models.CharField(verbose_name=_('Location'), max_length=100, blank=True)
    budget_from = models.PositiveIntegerField(verbose_name=_('Budget from'), null=True)
    budget_to = models.PositiveIntegerField(verbose_name=_('Budget to'), null=True)
    JOB_STATUS_CHOICES = (
        (0, _('Archived')),
        (1, _('Closed')),
        (2, _('Open'))
    )
    status = models.IntegerField(choices=JOB_STATUS_CHOICES, default=0)
    JOB_TYPES = (
        ('pt', _('Part Time')),
        ('ft', _('Full Time')),
        ('ct', _('Contract'))
    )
    type = models.CharField(max_length=2, choices=JOB_TYPES)
    category = models.ForeignKey(Category)
    approved = models.BooleanField(verbose_name=_('Approved by admin'), default=False)

    class Meta:
        ordering = ('-created_on', )
        verbose_name = _('Job Post')
        verbose_name_plural = _('Job Posts')


class JobPostPlugin(CMSPlugin):
    jobpost = models.ForeignKey('careers.JobPost', related_name='plugins')

    def __unicode__(self):
        return self.jobpost.title


class JobPostApplied(models.Model):
    jobpost = models.ForeignKey(JobPost)
    applicant = models.ForeignKey('users.User')
    date = models.DateTimeField(_('Applied'), editable=False, auto_now_add=True)
    resume = models.FileField(storage=fs, verbose_name=_('Upload resume'))
    message = models.ForeignKey('django_messages.Message')
