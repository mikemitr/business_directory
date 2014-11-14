from profiles.models import CompanyProfile
from django.db import models
from django.utils.translation import ugettext_lazy as _
from cms.models import CMSPlugin

import datetime


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
    category = models.ForeignKey(Category)

    class Meta:
        ordering = ('-created_on', )
        verbose_name = _('Job Post')
        verbose_name_plural = _('Job Posts')


class JobPostPlugin(CMSPlugin):
    jobpost = models.ForeignKey('careers.JobPost', related_name='plugins')

    def __unicode__(self):
      return self.jobpost.title