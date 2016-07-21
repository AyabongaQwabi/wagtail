# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-07-21 07:17
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0013_make_rendition_upload_callable'),
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='eventspage',
            name='celeb',
            field=models.CharField(default='teve', max_length=250),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='eventspage',
            name='celeb_image',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image'),
        ),
    ]
