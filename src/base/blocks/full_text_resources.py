from django.db import models
from django.utils.translation import gettext_lazy as _
from wagtail_link_block.blocks import LinkBlock

from wagtail.admin.panels import FieldPanel, InlinePanel, MultiFieldPanel
from wagtail.blocks import (
    CharBlock,
    RawHTMLBlock,
    RichTextBlock,
    StreamBlock,
    StructBlock,
    URLBlock,
)
from wagtail.blocks.struct_block import StructBlockAdapter
from wagtail.documents.blocks import DocumentChooserBlock
from wagtail.embeds.blocks import EmbedBlock
from wagtail.fields import RichTextField, StreamField
from wagtail.images.blocks import ImageChooserBlock
from wagtail.models import Page
from wagtail.snippets.models import register_snippet
from wagtail.snippets.views.snippets import SnippetViewSet


class FullTextResource(StructBlock):
    name = CharBlock(
        required=True,
        label=_("Текст"),
        max_length=1000,
    )
    img = ImageChooserBlock(required=True, label=_("Изображение"))
    link = URLBlock(
        label=_("Ссылка на ресурс"),
        max_length=255,
    )

    class Meta:
        label = "Ресурс"
        closed = True
        icon = "doc-full-inverse"
        template = "blocks/full_text_resource.html"


class FullTextResources(StructBlock):
    fulltextresources = StreamBlock(
        [
            (
                "fulltextresource",
                FullTextResource(
                    required=True,
                ),
            )
        ],
        label="Ресурсы",
        max_num=10,
        help_text="Максимальное количество ресурсов 10",
    )

    class Meta:
        label = "Ресурсы"
        closed = True
        icon = "doc-full-inverse"
        template = "blocks/full_text_resources.html"
