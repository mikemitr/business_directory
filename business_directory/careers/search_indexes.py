import datetime
from haystack import indexes
from .models import JobPost


class JobPostIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    budget_from = indexes.IntegerField(model_attr='budget_from')
    category = indexes.CharField(model_attr='category')
    company = indexes.CharField(model_attr='company')

    def get_model(self):
        return JobPost

    def prepare_company(self, obj):
        return "%s" % obj.company.company_name

    def index_queryset(self, using=None):
        job_reverse = dict((v, k) for k, v in JobPost.JOB_STATUS_CHOICES)
        return self.get_model().objects.filter(status=job_reverse['Open'])