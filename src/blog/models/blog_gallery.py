from django.db import models
from django.utils.translation import gettext_lazy as _
from modelcluster.fields import ParentalKey

from wagtail.admin.panels import FieldPanel
from wagtail.models import Orderable

from .blog_page import BlogPage


class BlogGallery(Orderable, models.Model):
    page = ParentalKey(
        BlogPage,
        related_name="gallery",
        on_delete=models.CASCADE,
    )
    image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
    )

    panels = [FieldPanel("image")]

    class Meta:
        verbose_name = _("Галерея блога")
        verbose_name_plural = _("Галерея блога")
