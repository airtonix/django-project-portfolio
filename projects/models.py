from datetime import datetime

from django.db import models
from django.db.models import permalink
from django.core.files.storage import FileSystemStorage
from django.utils.translation import ugettext_lazy as _

from adminsortable.models import Sortable
from sorl import thumbnail as sorl

from . import fields
from . import settings
from . import mixins


fs = FileSystemStorage(
    location=settings.PROJECT_UPLOAD_ROOT,
    base_url=settings.PROJECT_UPLOAD_URL)



class Endorsement(Sortable, mixins.SluggedModel):
    """
    Endorsement data
    """
    detail_urlname = 'project-endorsement-detail'

    person = models.CharField(max_length=100)
    client = models.ForeignKey("projects.Client")
    endorsement = models.TextField()

    class Meta:
        ordering = ['order', ]
        auto_created = False

    def __unicode__(self):
        """ Unicode representation for object. """
        return self.person


class Technology(Sortable, mixins.TaggedModel, mixins.SluggedModel):
    """
    A technology
    """
    detail_urlname = 'project-technology-detail'

    name = models.CharField(max_length=100)
    description = models.TextField()
    url = models.URLField()
    primary_technology = models.BooleanField(default=True)

    class Meta:
        ordering = ['order', ]
        auto_created = False

    def __unicode__(self):
        """ Unicode representation for object. """
        return self.name


class Collection(Sortable, mixins.TaggedModel, mixins.SluggedModel):
    """ A collection of projects. """
    detail_urlname = 'projects-collection-detail'

    title = models.CharField(_('title'), max_length=255)
    description = models.TextField(_('description'), blank=True)

    class Meta(Sortable.Meta):
        verbose_name = _('collection')
        verbose_name_plural = _('collections')
        auto_created = False

    def __unicode__(self):
        """ Unicode representation for object. """
        return self.title


class Client(Sortable, mixins.TaggedModel, mixins.SluggedModel):
    """ A collection of clients. """
    detail_urlname = 'project-client-detail'

    title = models.CharField(_('title'), max_length=255)
    image = sorl.ImageField(upload_to='uploads/clients/images/')
    description = models.TextField(_('description'), blank=True)

    class Meta(Sortable.Meta):
        verbose_name = _('client')
        verbose_name_plural = _('clients')

    def __unicode__(self):
        """ Unicode representation for object. """
        return self.title


class ProjectManager(models.Manager):
    def get_queryset(self):
        return super(ProjectManager, self).get_queryset()

    def concepts(self):
        return self.get_queryset().filter(phase = 'concept')

    def private_beta(self):
        return self.get_queryset().filter(phase = 'private_beta')

    def public_beta(self):
        return self.get_queryset().filter(phase = 'private_beta')

    def published(self):
        return self.get_queryset().filter(phase = 'published')

    def inactive(self):
        return self.get_queryset().filter(phase = 'inactive')


class Project(Sortable, mixins.TaggedModel, mixins.SluggedModel, mixins.TimeStampedModel):
    """
    A project
    """
    detail_urlname = 'project-detail'

    image = sorl.ImageField(storage=fs, upload_to='uploads/project/image', blank=True, null=True,
        help_text=_("Banner graphic for this project, store all your other images as screenshots"))

    title = models.CharField(max_length=100)
    summary = models.TextField()
    body = models.TextField()

    phase = models.CharField(max_length=32, choices=settings.PROJECT_PHASES)

    author = models.ForeignKey("auth.User", blank=True, null=True)

    client = models.CharField(max_length=100, blank=True)
    url = models.URLField(blank=True, null=True)
    launch_date = models.DateField(blank=True, null=True)
    featured = models.BooleanField(default=True)

    technologies = models.ManyToManyField("projects.Technology", related_name='projects', blank=True, null=True)
    endorsements = models.ManyToManyField("projects.Endorsement", related_name='projects', blank=True, null=True)
    collection = models.ForeignKey("projects.Collection", related_name='projects', blank=True, null=True)

    objects = ProjectManager()

    class Meta:
        ordering = ['order', ]

    def __init__(self, *args, **kwargs):
        super(Project, self).__init__(*args, **kwargs)
        self._teaser = None

    def __unicode__(self):
        """ Unicode representation for object. """
        return self.title


    def _get_teaser(self):
        """
        Retrieve some part of the project or the projects's summary.
        """

        if not self._teaser:
            if len(self.description.strip()):
                text = self.description
            else:
                text = self.rendered_content
            word_limit = settings.PROJECT_TEASER_WORD_LIMIT
            words = text.split(' ')
            if len(words) > word_limit:
                text = '%s...' % ' '.join(words[:word_limit])
            self._teaser = text

        return self._teaser
    teaser = property(_get_teaser)

    def _get_thumbnail(self):
        if not self.image:
            return settings.PROJECT_DEFAULT_THUMBNAIL_URL
        return self.image
    thumbnail = property(_get_thumbnail)


class Image(Sortable, mixins.TaggedModel, mixins.PkModel):
    """
    A related image to a project
    """
    project = models.ForeignKey("projects.Project", related_name="images")
    image = sorl.ImageField(upload_to='uploads/projects/images/')

    class Meta:
        ordering = ['order', ]

    def __unicode__(self):
        """ Unicode representation for object. """
        return self.image

