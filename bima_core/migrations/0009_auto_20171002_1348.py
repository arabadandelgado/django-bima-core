# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-10-02 11:48
from __future__ import unicode_literals

import bima_core.fields
import bima_core.models
import bima_core.storage
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bima_core', '0008_auto_20170728_1536'),
    ]

    operations = [
        migrations.AddField(
            model_name='photo',
            name='video_thumbnail',
            field=models.ImageField(
                blank=True,
                null=True,
                max_length=200,
                upload_to=bima_core.models.Photo.video_thumbnail_path, verbose_name='Video thumbnail',
            ),
        ),
    ]
