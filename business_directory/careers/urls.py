from django.conf.urls import patterns, url, include
from careers import views
from haystack.forms import FacetedSearchForm
from haystack.query import SearchQuerySet
from haystack.views import FacetedSearchView

sqs = SearchQuerySet().facet('type').facet('category')

urlpatterns = patterns('',
    # URL pattern for the CategoryListView
    url(
        regex=r'^categories/$',
        view=views.CategoryListView.as_view(),
        name='categories'
    ),
    # URL pattern for the CategoryDetailView
    url(
        regex=r'^category/(?P<slug>[\w-]+)/$',
        view=views.CategoryDetailView.as_view(),
        name='category'
    ),

    # URL pattern for the JobPostListView
    url(
        regex=r'^jobposts/$',
        view=views.JobPostListView.as_view(),
        name='posts',
    ),
    # URL pattern for the JobPostDetailView
    url(
        regex=r'^jobpost/(?P<pk>[\w.@+-]+)/$',
        view=views.JobPostDetailView.as_view(),
        name='post'
    ),
    # URL pattern for the JobPostCreateView
    url(
        regex=r'^add-jobpost/$',
        view=views.JobPostCreateView.as_view(),
        name='add_jobpost'
    ),

    url(r'^$', FacetedSearchView(form_class=FacetedSearchForm, searchqueryset=sqs), name='haystack_search'),
    # url(r'', include('haystack.urls')),
    url(
        regex=r'^applicants/$',
        view=views.JobPostAppliedListView.as_view(),
        name='applicants'
    ),
    url(
        regex=r'^applicant/(?P<pk>[\w.@+-]+)/$',
        view=views.JobPostAppliedDetailView.as_view(),
        name='applicant'
    ),

    url(r'^messages/', include('django_messages.urls')),
)