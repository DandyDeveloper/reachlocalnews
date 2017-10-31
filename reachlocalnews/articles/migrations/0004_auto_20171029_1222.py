# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-29 12:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0003_auto_20171029_1207'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='published_date',
            new_name='publishedAt',
        ),
        migrations.RenameField(
            model_name='article',
            old_name='article_url',
            new_name='url',
        ),
        migrations.RenameField(
            model_name='article',
            old_name='image_url',
            new_name='urlToImage',
        ),
        migrations.AlterField(
            model_name='article',
            name='author',
            field=models.CharField(max_length=50),
        ),
    ]
