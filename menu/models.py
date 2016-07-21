from django.db import models

from wagtail.wagtailcore.models import Page
from wagtail.wagtailcore.fields import StreamField
from wagtail.wagtailcore import blocks
from wagtail.wagtailadmin.edit_handlers import FieldPanel, StreamFieldPanel
from wagtail.wagtailimages.blocks import ImageChooserBlock

class MenuPage(Page):

  class DishBlock(blocks.StructBlock):
          name=blocks.CharBlock(required=True)
          demo=ImageChooserBlock()
          class Meta:
              icon='user'

  body = StreamField([
      ('dish',DishBlock())
   ],null=True,blank=True)


  content_panels = Page.content_panels + [
      StreamFieldPanel('body')
  ]
