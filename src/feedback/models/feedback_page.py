from django.db import models
from django.shortcuts import render
from django.utils.translation import gettext_lazy as _
from modelcluster.fields import ParentalKey

from wagtail.admin.panels import FieldPanel
from wagtail.fields import RichTextField
from wagtail.models import Orderable, Page

from ..forms import FeedbackForm


class FeedbackPage(Page):
    intro = RichTextField(_("Текст на странице формы"), blank=True)
    success_text = RichTextField(
        _("Текст на странице благодарности"), blank=True
    )

    content_panels = Page.content_panels + [
        FieldPanel("intro"),
        FieldPanel("success_text"),
    ]

    def serve(self, request):
        if request.method == "POST":
            form = FeedbackForm(request.POST)
            if form.is_valid():
                feedback_data = form.save()
                return render(
                    request,
                    "pages/success.html",
                    {
                        "page": self,
                        "feedback_data": feedback_data,
                    },
                )
        else:
            form = FeedbackForm()

        return render(
            request,
            "pages/feedback.html",
            {
                "page": self,
                "form": form,
            },
        )

    class Meta:
        verbose_name = _("Обратная связь")
        verbose_name_plural = _("Общие настройки")
