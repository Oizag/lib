from django.db import models
from django.utils.translation import gettext_lazy as _
from wagtail_link_block.blocks import LinkBlock

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


class Button(StructBlock):
    text = CharBlock(
        required=True,
        label=_("Текст кнопки"),
        max_length=255,
    )

    link = LinkBlock(
        required=True,
        label=_(" "),
        max_length=255,
        closed=True,
    )
    classes = CharBlock(
        required=False,
        label=_("Дополнительные классы"),
        help_text=_(
            "Дополнительные CSS классы.\
                    Вводятся через пробел"
        ),
        max_length=255,
    )

    class Meta:
        label = "Кнопка"
        closed = True
        icon = "bold"
        template = "blocks/button.html"
