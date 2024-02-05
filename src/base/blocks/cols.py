from django.db import models
from django.utils.translation import gettext_lazy as _
from wagtail_link_block.blocks import LinkBlock

from wagtail.admin.panels import FieldPanel, InlinePanel, MultiFieldPanel
from wagtail.blocks import (
    CharBlock,
    IntegerBlock,
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

from .button import Button
from .documents import Documents


class Cols(StructBlock):
    class_column = CharBlock(
        verbose_name="Классы для разметки колонок",
        help_text="Пример: col-12 col-md-6 col-lg-4",
        max_length=30,
    )
    content = StreamBlock(
        [
            (
                "content",
                RichTextBlock(),
            ),
            (
                "html_code",
                RawHTMLBlock(),
            ),
            (
                "button",
                Button(),
            ),
            (
                "documents",
                Documents(),
            ),
        ],
        label="Контент",
        max_num=10,
        help_text="Максимальное количество документов 10",
    )

    class Meta:
        label = "Колоночный контент"
        closed = True
        template = "blocks/cols.html"
