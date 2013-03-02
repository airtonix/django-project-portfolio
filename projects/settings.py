from django.conf import settings
from django.utils.translation import ugettext_lazy as _

PROJECT_PHASES = getattr(settings, 'PROJECT_PHASES', (
    ('concept', _("Concept")),
    ('private_beta', _("Private Beta")),
    ('public_beta', _("Public Beta")),
    ('release', _("Released")),
))

PROJECT_UPLOAD_ROOT = getattr(settings, 'MEDIA_ROOT', 'files')
PROJECT_UPLOAD_URL = getattr(settings, 'MEDIA_URL', 'files')
PROJECT_DEFAULT_THUMBNAIL_URL = "http://placehold.it/128x128/&text=:)"
PROJECT_TEASER_WORD_LIMIT = 72

MARKUP_HTML = 'h'
MARKUP_MARKDOWN = 'm'
MARKUP_REST = 'r'
MARKUP_TEXTILE = 't'
MARKUP_OPTIONS = getattr(settings, 'ARTICLE_MARKUP_OPTIONS', (
        (MARKUP_HTML, _('HTML/Plain Text')),
        (MARKUP_MARKDOWN, _('Markdown')),
        (MARKUP_REST, _('ReStructured Text')),
        (MARKUP_TEXTILE, _('Textile'))
    ))
MARKUP_DEFAULT = getattr(settings, 'ARTICLE_MARKUP_DEFAULT', MARKUP_HTML)
MARKUP_HELP = _("""Select the type of markup you are using in this article.
<ul>
<li><a href="http://daringfireball.net/projects/markdown/basics" target="_blank">Markdown Guide</a></li>
<li><a href="http://docutils.sourceforge.net/docs/user/rst/quickref.html" target="_blank">ReStructured Text Guide</a></li>
<li><a href="http://thresholdstate.com/articles/4312/the-textile-reference-manual" target="_blank">Textile Guide</a></li>
</ul>""")