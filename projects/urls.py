from django.conf.urls.defaults import patterns
from surlex.dj import surl

from . import views

urlpatterns = patterns('',

    surl(r'^projects/$', views.ProjectListView.as_view(), name='project-list'),
    surl(r'^project/<slug:s>/$', views.ProjectDetailView.as_view(), name='project-detail'),

    surl(r'^technologies/$', views.TechnologyListView.as_view(), name='project-technology-list'),
    surl(r'^technology/<slug:s>/$', views.TechnologyDetailView.as_view(), name='project-technology-detail'),

    surl(r'^clients/$', views.ClientListView.as_view(tags=("client", )), name='project-client-list'),
    surl(r'^client/<slug:s>/$', views.ClientDetailView.as_view(), name='project-client-detail'),

    surl(r'^partners/$', views.ClientListView.as_view(tags=("partner", )), name='project-partner-list'),
    surl(r'^partner/<slug:s>/$', views.ClientDetailView.as_view(), name='project-partner-detail'),

    surl(r'^collections/$', views.CollectionListView.as_view(), name='project-collection-list'),
    surl(r'^collection/<slug:s>/$', views.CollectionDetailView.as_view(), name='project-collection-detail'),

    surl(r'^endorsements/$', views.EndorsementListView.as_view(), name='project-endorsement-list'),
    surl(r'^endorsement/<slug:s>/$', views.EndorsementDetailView.as_view(), name='project-endorsement-detail'),

    surl(r'^images/$', views.EndorsementListView.as_view(), name='project-image-list'),
    surl(r'^image/<pk:#>/$', views.EndorsementDetailView.as_view(), name='project-image-detail'),
)
