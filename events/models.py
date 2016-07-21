from __future__ import unicode_literals

from django.db import models
from django.db import models
from wagtail.wagtailcore.models import Page
from wagtail.wagtailcore.fields import RichTextField
from wagtail.wagtailadmin.edit_handlers import FieldPanel , MultiFieldPanel
from wagtail.wagtailimages.edit_handlers import ImageChooserPanel


class EventsPage(Page):
    date = models.DateField('When is the Event ?')
    host = models.CharField(max_length=250)
    location=RichTextField(blank=False)
    celeb = models.CharField(max_length=250)
    celeb_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    content_panels = Page.content_panels + [
        FieldPanel('date'),
        FieldPanel('host'),
        FieldPanel('location'),
        MultiFieldPanel(
            [
                FieldPanel('celeb'),
                ImageChooserPanel('celeb_image')
            ],
            heading="Celebrities",
            classname="collapsible collapsed"
        )
    ]
