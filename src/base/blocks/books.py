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


class Book(StructBlock):
    title = CharBlock(
        required=True,
        label=_("О книге"),
        max_length=255,
    )
    img = ImageChooserBlock(required=True, label=_("Изображение"))
    text = CharBlock(
        required=True,
        label=_("Описание"),
    )

    class Meta:
        label = "Книга"
        closed = True
        icon = "doc-full-inverse"
        template = "blocks/book.html"


class Books(StructBlock):
    books = StreamBlock(
        [
            (
                "book",
                Book(
                    required=True,
                ),
            )
        ],
        label="Книги",
        max_num=5,
        help_text="Максимальное количество книг 5",
    )

    class Meta:
        label = "Книги"
        closed = True
        icon = "doc-full-inverse"
        template = "blocks/books.html"