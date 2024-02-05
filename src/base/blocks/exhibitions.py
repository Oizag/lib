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


class Exhibition(StructBlock):
    title = CharBlock(
        required=True,
        label=_("Заголовок"),
        max_length=255,
    )
    img = ImageChooserBlock(required=True, label=_("Изображение"))
    text = CharBlock(
        required=True,
        label=_("Текст"),
    )
    exhibition_place = CharBlock(
        required=True,
        label=_("Место представления выставки"),
        max_length=255,
    )
    address = CharBlock(
        required=True,
        label=_("Адрес"),
        max_length=255,
    )

    class Meta:
        label = "Выставка"
        closed = True
        icon = "doc-full-inverse"
        template = "blocks/exhibition.html"


class Exhibitions(StructBlock):
    exhibitions = StreamBlock(
        [
            (
                "exhibition",
                Exhibition(
                    required=True,
                ),
            )
        ],
        label="Выставки",
        max_num=10,
        help_text="Максимальное количество выставок 10",
    )

    class Meta:
        label = "Выставки"
        closed = True
        icon = "doc-full-inverse"
        template = "blocks/exhibitions.html"