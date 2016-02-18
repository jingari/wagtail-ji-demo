# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import wagtail.wagtailcore.fields
import wagtail.wagtailcore.blocks
import wagtail.wagtailimages.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0001_squashed_0016_change_page_url_path_to_text_field'),
        ('home', '0005_auto_20150811_2148'),
    ]

    operations = [
        migrations.CreateModel(
            name='ParallaxPage',
            fields=[
                ('page_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('body', wagtail.wagtailcore.fields.StreamField([('heading', wagtail.wagtailcore.blocks.CharBlock(classname='full title')), ('paragraph', wagtail.wagtailcore.blocks.RichTextBlock()), ('image', wagtail.wagtailimages.blocks.ImageChooserBlock()), ('pullquote', wagtail.wagtailcore.blocks.StructBlock([(b'quote_text', wagtail.wagtailcore.blocks.TextBlock()), (b'quote_author', wagtail.wagtailcore.blocks.TextBlock())])), ('parallax', wagtail.wagtailcore.blocks.StructBlock([(b'parallax_image', wagtail.wagtailimages.blocks.ImageChooserBlock()), (b'parallax_text', wagtail.wagtailcore.blocks.RichTextBlock())]))])),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
    ]
