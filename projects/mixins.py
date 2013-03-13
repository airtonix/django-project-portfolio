from datetime import datetime

from django.db import models
from django.db.models import permalink
from django.utils.translation import ugettext_lazy as _

from taggit.managers import TaggableManager

from . import settings


class ExpirableContentModel(models.Model):
    is_active = models.BooleanField(default = False)
    publish_date = models.DateTimeField(default=datetime.now,
        help_text=_('The date and time this article shall appear online.'))
    expiration_date = models.DateTimeField(blank=True, null=True,
        help_text=_('Leave blank if the article does not expire.'))

    class Meta:
        abstract = True

    def __init__(self, *args, **kwargs):
        """Makes sure that we have some rendered content to use"""

        super(ExpirableContentModel, self).__init__(*args, **kwargs)

        if self.id:
            if self.expiration_date and self.expiration_date <= datetime.now() and self.is_active:
                self.is_active = False
                self.save()

class RenderedContentModel(models.Model):
    rendered_content = models.TextField()
    markup = models.CharField(max_length=1,
        choices=settings.MARKUP_OPTIONS,
        default=settings.MARKUP_DEFAULT,
        help_text=settings.MARKUP_HELP)

    class Meta:
        abstract = True

    def __init__(self, *args, **kwargs):
        """Makes sure that we have some rendered content to use"""

        super(RenderedContentModel, self).__init__(*args, **kwargs)

        if self.id:
            if not self.rendered_content or not len(self.rendered_content.strip()):
                self.save()

    def save(self, *args, **kwargs):
        using = kwargs.get('using', settings.DEFAULT_DB)
        self.render_markup()
        super(RenderedContentModel, self).save(*args, **kwargs)

    def render_markup(self, *args, **kwargs):
        """Turns any markup into HTML"""

        original = self.rendered_content
        if self.markup == settings.MARKUP_MARKDOWN:
            self.rendered_content = markup.markdown(self.content)
        elif self.markup == settings.MARKUP_REST:
            self.rendered_content = markup.restructuredtext(self.content)
        elif self.markup == settings.MARKUP_TEXTILE:
            self.rendered_content = markup.textile(self.content)
        else:
            self.rendered_content = self.content

        return (self.rendered_content != original)



class TimeStampedModel(models.Model):
    """
    An abstract base class model that provides self-managed "created" and
    "modified" fields, borrowed from django_extensions.
    """
    created = models.DateTimeField(_('created'), auto_now_add=True)
    modified = models.DateTimeField(_('modified'), auto_now=True)
    published = models.DateTimeField(_('published'), null=True, blank=True)

    class Meta:
        abstract = True



class PkModel(models.Model):

    class Meta:
        abstract = True

    @permalink
    def get_absolute_url(self):
        return (self.detail_urlname, (), {
            "pk": self.pk })


class SluggedModel(models.Model):
    slug = models.SlugField(_('slug'), unique=True)

    class Meta:
        abstract = True

    @permalink
    def get_absolute_url(self):
        return (self.detail_urlname, (), {
            "slug": self.slug })

    def save(self, *args, **kwargs):
        # self.do_unique_slug(using)
        super(SluggedModel, self).save(*args, **kwargs)

    # def do_unique_slug(self, using=DEFAULT_DB):
    #     """
    #     Ensures that the slug is always unique for the year this article was
    #     posted
    #     """

    #     if not self.id:
    #         # make sure we have a slug first
    #         if not len(self.slug.strip()):
    #             self.slug = slugify(self.title)

    #         self.slug = self.get_unique_slug(self.slug, using)
    #         return True

    #     return False

    # def get_unique_slug(self, slug):
    #     """Iterates until a unique slug is found"""

    #     # we need a publish date before we can do anything meaningful
    #     if type(self.published) is not datetime:
    #         return slug

    #     orig_slug = slug
    #     year = self.published.year
    #     counter = 1

    #     while True:
    #         not_unique = self.objects.all()
    #         if hasattr(not_unique, 'using'):
    #             not_unique = not_unique.using(using)
    #         not_unique = not_unique.filter(published__year=year, slug=slug)

    #         if len(not_unique) == 0:
    #             return slug

    #         slug = '%s-%s' % (orig_slug, counter)
    #         counter += 1


class TaggedModel(models.Model):
    tags = TaggableManager(blank=True)

    class Meta:
        abstract = True
