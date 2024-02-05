from django.db import models
from django.utils.translation import gettext_lazy as _

from base.blocks import BaseStreamBlock
from wagtail.admin.panels import FieldPanel, InlinePanel, MultiFieldPanel
from wagtail.blocks import CharBlock, RichTextBlock
from wagtail.contrib.routable_page.models import RoutablePageMixin, route
from wagtail.embeds.blocks import EmbedBlock
from wagtail.fields import RichTextField, StreamField
from wagtail.images.blocks import ImageChooserBlock
from wagtail.models import Page
from wagtail.search import index

from .blog_page import BlogPage


class BlogIndexPage(RoutablePageMixin, Page):
    """
    Index page for blogs.
    We need to alter the page model's context to return the child page objects,
    the BlogPage objects, so that it works as an index page
    """

    image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
    )

    content_panels = Page.content_panels + [
        FieldPanel("image"),
    ]

    subpage_types = ["BlogPage"]

    def children(self):
        return self.get_children().specific().live()

    def get_context(self, request):
        context = super(BlogIndexPage, self).get_context(request)
        context["posts"] = (
            BlogPage.objects.descendant_of(self)
            .live()
            .order_by("-date_published")
        )
        return context

    def serve_preview(self, request, mode_name):
        return self.serve(request)

    def get_posts(self):
        posts = BlogPage.objects.live().descendant_of(self)
        return posts


    class Meta:
        verbose_name = _("Блог")
        verbose_name_plural = _("Блоги")