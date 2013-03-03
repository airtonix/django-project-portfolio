from django.http import Http404
from django.views.generic import View, TemplateView, ListView, DetailView
from django.views.generic.edit import UpdateView, CreateView, DeleteView, FormView
from django.core.urlresolvers import reverse

from .lib.lazy import reverse_lazy
from . import models

class TaggableListViewMixin(object):
    tags = None

    def get_queryset(self):
        queryset = super(TaggableListViewMixin, self).get_queryset()
        if getattr(self, "tags"):
            queryset = queryset.filter(tags__name__in=self.tags)
        return queryset


class ProjectViewBase(object):
    model = models.Project

class ProjectListView(TaggableListViewMixin, ProjectViewBase, ListView): pass

class ProjectConceptListView(TaggableListViewMixin, ProjectViewBase, ListView):

    def get_queryset(self):
        queryset = super(ProjectConceptListView, self).get_queryset()
        return queryset.filter(phase="concept")

class ProjectDetailView(ProjectViewBase, DetailView): pass



class TechnologyViewBase(object):
    model = models.Technology

class TechnologyListView(TaggableListViewMixin, TechnologyViewBase, ListView): pass

class TechnologyDetailView(TechnologyViewBase, DetailView): pass



class ClientViewBase(object):
    model = models.Client

class ClientListView(TaggableListViewMixin, ClientViewBase, ListView): pass

class ClientDetailView(ClientViewBase, DetailView): pass



class CollectionViewBase(object):
    model = models.Collection

class CollectionListView(TaggableListViewMixin, CollectionViewBase, ListView): pass

class CollectionDetailView(CollectionViewBase, DetailView): pass



class EndorsementViewBase(object):
    model = models.Endorsement

class EndorsementListView(TaggableListViewMixin, EndorsementViewBase, ListView): pass

class EndorsementDetailView(EndorsementViewBase, DetailView): pass



class ImageViewBase(object):
    model = models.Image

class ImageListView(TaggableListViewMixin, ImageViewBase, ListView): pass

class ImageDetailView(ImageViewBase, DetailView): pass

