# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-30 17:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0008_auto_20171030_0931'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='publishedAt',
            field=models.DateTimeField(),
        ),
    ]
