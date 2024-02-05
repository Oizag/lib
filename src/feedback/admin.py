from wagtail.admin.panels import FieldPanel
from wagtail.admin.ui.tables import UpdatedAtColumn
from wagtail.snippets.models import register_snippet
from wagtail.snippets.views.snippets import SnippetViewSet

from .models import Feedback


class FeedbackViewSet(SnippetViewSet):
    model = Feedback
    icon = "mail"
    list_display = [
        "name",
        "email",
        "text",
    ]
    list_per_page = 15
    add_to_admin_menu = True


register_snippet(FeedbackViewSet)
