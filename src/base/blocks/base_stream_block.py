from django.utils.translation import gettext_lazy as _

from wagtail.blocks import RawHTMLBlock, RichTextBlock, StreamBlock
from wagtail.embeds.blocks import EmbedBlock
from wagtail.fields import StreamField
from wagtail.images.blocks import ImageChooserBlock

from .button import Button
from .cols import Cols
from .documents import Documents
from .full_text_resources import FullTextResources
from .exhibitions import Exhibitions
from .books import Books


class BaseStreamBlock(StreamBlock):
    """
    Define the custom blocks that `StreamField` will utilize
    """

    text = RichTextBlock(label=("Текст"))
    html_code = RawHTMLBlock(label=("Код"))
    image_block = ImageChooserBlock(label=("Изображение"))
    embed_block = EmbedBlock(label=("Видео"))
    button = Button()
    documents = Documents()
    cols = Cols()
    full_text_resources = FullTextResources()
    exhibitions = Exhibitions()
    books = Books()
