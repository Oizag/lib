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


class Document(StructBlock):
    name = CharBlock(
        required=True,
        label=_("Название документа"),
        max_length=255,
    )
    file = DocumentChooserBlock(required=True, label=_("Файл"))

    class Meta:
        label = "Документ"
        closed = True
        icon = "doc-full-inverse"
        template = "blocks/document.html"


class Documents(StructBlock):
    documents = StreamBlock(
        [
            (
                "document",
                Document(
                    required=True,
                ),
            )
        ],
        label="Документы",
        max_num=10,
        help_text="Максимальное количество документов 10",
    )

    class Meta:
        label = "Документы"
        closed = True
        icon = "doc-full-inverse"
        template = "blocks/documents.html"
