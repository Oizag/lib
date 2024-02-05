from django.db import models
from django.utils.translation import gettext_lazy as _

from wagtail.admin.panels import FieldPanel, InlinePanel, MultiFieldPanel
from wagtail.blocks import (
    CharBlock,
    RawHTMLBlock,
    RichTextBlock,
    StructBlock,
    URLBlock,
)
from wagtail.blocks.struct_block import StructBlockAdapter
from wagtail.embeds.blocks import EmbedBlock
from wagtail.fields import RichTextField, StreamField
from wagtail.images.blocks import ImageChooserBlock
from wagtail.models import Page
from wagtail.snippets.models import register_snippet
from wagtail.snippets.views.snippets import SnippetViewSet

from ..blocks import BaseStreamBlock


class SimplePage(Page):
    template = "pages/simple.html"
    body = StreamField(
        BaseStreamBlock(),
        use_json_field=True,
        blank=True,
        null=True,
        verbose_name=_("Контент"),
    )

    content_panels = Page.content_panels + [
        FieldPanel("body"),
    ]

    class Meta:
        verbose_name = _("Простая страница")
        verbose_name_plural = _("Простые страницы")
