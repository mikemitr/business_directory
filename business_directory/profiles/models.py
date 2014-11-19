from django.conf import settings
from django.db import models
from django.utils.translation import ugettext_lazy as _


class CompanyProfile(models.Model):
    # Default user profile
    # If we do this we need to either have a post_save signal or
    #     redirect to a profile_edit view on initial login.
    user = models.OneToOneField(settings.AUTH_USER_MODEL, related_name='company')
    company_name = models.CharField(_('company name'), max_length=255)
    # more company profile fields here

    def __unicode__(self):
        return self.company_name

 
class EmployeeProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, related_name='employee')
    first_name = models.CharField(_('first name'), max_length=255)
    last_name = models.CharField(_('last name'), max_length=255)
    # more employee profile fields here