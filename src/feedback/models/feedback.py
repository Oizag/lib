from django.db import models
from django.utils.translation import gettext_lazy as _
from modelcluster.fields import ParentalKey

from wagtail.admin.panels import FieldPanel
from wagtail.models import Orderable, Page, PreviewableMixin
from wagtail.search import index
from wagtail.snippets.models import register_snippet


class Feedback(PreviewableMixin, models.Model):
    name = models.CharField(_("Имя"), max_length=255)
    email = models.EmailField(_("E-mail"), max_length=255)
    text = models.TextField(_("Текст обращения"))

    panels = [
        FieldPanel("name"),
        FieldPanel("email"),
        FieldPanel("text"),
    ]

    search_fields = [
        index.SearchField("name"),
        index.SearchField("email"),
    ]

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = _("Обратная связь")
        verbose_name_plural = _("Обратная связь")
