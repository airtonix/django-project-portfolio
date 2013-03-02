from django.http import Http404
from django.views.generic import View, TemplateView, ListView, DetailView
from django.views.generic.edit import UpdateView, CreateView, DeleteView, FormView
from django.core.urlresolvers import reverse

from .lib.lazy import reverse_lazy
    
from . import models


class ProjectViewBase(object):
    model = models.Project

class ProjectListView(ListView):
    model = models.Project
    tags = None
    def get_queryset(self):
        queryset = super(ProjectListView, self).get_queryset()
        if getattr(self, "tags"):
            queryset = queryset.filter(tags__name__in=self.tags)
        return queryset

class ProjectDetailView(ProjectViewBase, DetailView): pass



class TechnologyViewBase(object):
    model = models.Technology

class TechnologyListView(TechnologyViewBase, ListView): pass

class TechnologyDetailView(TechnologyViewBase, DetailView): pass



class ClientViewBase(object):
    model = models.Client

class ClientListView(ClientViewBase, ListView): 
    tags = None

    def get_queryset(self):
        queryset = super(ClientListView, self).get_queryset()
        if getattr(self, "tags"):
            queryset = queryset.filter(tags__name__in=self.tags)
        return queryset

class ClientDetailView(ClientViewBase, DetailView): pass



class CollectionViewBase(object):
    model = models.Collection

class CollectionListView(CollectionViewBase, ListView): pass

class CollectionDetailView(CollectionViewBase, DetailView): pass



class EndorsementViewBase(object):
    model = models.Endorsement

class EndorsementListView(EndorsementViewBase, ListView): pass

class EndorsementDetailView(EndorsementViewBase, DetailView): pass



class ImageViewBase(object):
    model = models.Image

class ImageListView(ImageViewBase, ListView): pass

class ImageDetailView(ImageViewBase, DetailView): pass

