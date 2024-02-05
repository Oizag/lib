from django.db import models
from django.utils.translation import gettext_lazy as _
from modelcluster.fields import ParentalKey
from modelcluster.models import ClusterableModel

from wagtail.admin.panels import (
    FieldPanel,
    InlinePanel,
    ObjectList,
    TabbedInterface,
    TitleFieldPanel,
)
from wagtail.contrib.settings.models import (
    BaseGenericSetting,
    BaseSiteSetting,
    register_setting,
)


@register_setting
class Settings(ClusterableModel, BaseGenericSetting):
    logo = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="settings",
        verbose_name=_("Логотип"),
    )

    other_tab_panels = [
        FieldPanel("logo"),
    ]

    edit_handler = TabbedInterface(
        [
            ObjectList(other_tab_panels, heading=_("Общее")),
        ]
    )

    class Meta:
        verbose_name = _("Общие настройки")
        verbose_name_plural = _("Общие настройки")