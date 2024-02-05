from django.db import models
from django.utils.translation import gettext_lazy as _

from base.blocks import BaseStreamBlock
from wagtail.admin.panels import (
    FieldPanel,
    InlinePanel,
    MultiFieldPanel,
    MultipleChooserPanel,
)
from wagtail.blocks import CharBlock, RichTextBlock
from wagtail.embeds.blocks import EmbedBlock
from wagtail.fields import RichTextField, StreamField
from wagtail.images.blocks import ImageChooserBlock
from wagtail.models import Page
from wagtail.search import index


class BlogPage(Page):
    introduction = models.TextField(
        help_text="Text to describe the page", blank=True
    )
    image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
        help_text="Landscape mode only; horizontal width between 1000px and 3000px.",
    )
    body = StreamField(
        BaseStreamBlock(),
        verbose_name="Page body",
        blank=True,
        use_json_field=True,
    )
    date_published = models.DateField(
        "Date article published", blank=True, null=True
    )

    content_panels = Page.content_panels + [
        FieldPanel("introduction"),
        FieldPanel("image"),
        FieldPanel("body"),
        FieldPanel("date_published"),
        MultipleChooserPanel(
            "gallery",
            chooser_field_name="image",
            heading="Галерея",
            label="Фото",
            max_num=10,
        ),
    ]

    search_fields = Page.search_fields + [
        index.SearchField("body"),
    ]

    def get_gallery(self):
        return [item.image for item in self.gallery.all()]

    # Specifies parent to BlogPage as being BlogIndexPages
    parent_page_types = ["BlogIndexPage"]

    # Specifies what content types can exist as children of BlogPage.
    # Empty list means that no child content types are allowed.
    subpage_types = []

    class Meta:
        verbose_name = _("Блог")
        verbose_name_plural = _("Блог")
