from __future__ import unicode_literals

from django.db import models

from wagtail.wagtailcore.models import Page
from wagtail.wagtailcore.fields import StreamField
from wagtail.wagtailcore import blocks
from wagtail.wagtailembeds.blocks import EmbedBlock
from wagtail.wagtailadmin.edit_handlers import FieldPanel, FieldRowPanel,MultiFieldPanel, InlinePanel, PageChooserPanel, StreamFieldPanel
from wagtail.wagtailimages.blocks import ImageChooserBlock




class HomePage(Page):
    pass

class PullQuoteBlock(blocks.StructBlock):
    quote_text = blocks.TextBlock()
    quote_author = blocks.TextBlock()

    class Meta:
        template = 'home/blocks/pullquote.html'

class ParallaxBlock(blocks.StructBlock):
    parallax_image = ImageChooserBlock()
    parallax_text = blocks.RichTextBlock()

    class Meta:
        template = 'home/blocks/parallax.html'

class CarouselBlock(blocks.StructBlock):
    image = ImageChooserBlock()
    text = blocks.RichTextBlock()

    class Meta:
        icon='cogs'
        template = 'home/blocks/carousel.html'

class ImageCarouselBlock(blocks.StructBlock):
    image = ImageChooserBlock()
    caption = blocks.TextBlock(required=False)

    class Meta:
        icon = 'image'



class ParallaxPage(Page):
    FieldPanel('title'),
    body = StreamField([
        ('heading', blocks.CharBlock(classname="full title")),
        ('paragraph', blocks.RichTextBlock()),
        ('image', ImageChooserBlock()),
        ('pullquote', PullQuoteBlock()),
        ('parallax', ParallaxBlock()),
        ('carousel', CarouselBlock()),
        ('image_carousel', blocks.ListBlock(ImageCarouselBlock(),template='home/blocks/imagecarousel.html',icon="image")),
    ])

    content_panels = [
        FieldPanel('title'),
        StreamFieldPanel('body'),
    ]

class BlogPage(Page):
    FieldPanel('title'),
    author = models.CharField(max_length=255)
    date = models.DateField("Post date")
    body = StreamField([
        ('heading', blocks.CharBlock(classname="full title")),
        ('paragraph', blocks.RichTextBlock()),
        ('image', ImageChooserBlock()),
        ('pullquote', PullQuoteBlock()),
    ])

    content_panels = [
        FieldPanel('title'),
        FieldPanel('author'),
        FieldPanel('date'),
        StreamFieldPanel('body'),
    ]