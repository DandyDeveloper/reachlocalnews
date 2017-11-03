# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models


class Source(models.Model):
    ''' Source model for sources '''
    source_id = models.CharField(max_length=35)
    name = models.CharField(max_length=50)

    def __unicode__(self):
        return 'Source: ' + str(self.id)


class Article(models.Model):
    ''' Article model for articles
        source: The article source
        author: The author(s) of the article
        title: Title of the article
        description: Snippet of articles (provided by API)
        url: URL to article
        urlToImage: Headline image from article (Can be empty)
        publishedAt: The published date. Sometimes missing, populated with import date.
    '''
    source = models.CharField(max_length=35)
    author = models.CharField(max_length=120, default='No author provided', blank=True)
    title = models.CharField(max_length=240)
    description = models.TextField(default='No description provided.', blank=True, null=True)
    url = models.URLField(max_length=300)
    urlToImage = models.URLField(max_length=500, null=True)
    publishedAt = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return 'Article: ' + str(self.id)

    def as_dict(self):
        ''' Returns dict from Article instance. Used by views
            to generate safe JSONResponse. '''
        return {
            "id": self.id,
            "source": self.source,
            "author": self.author,
            "title": self.title,
            "description": self.description,
            "url": self.url,
            "image_url": self.urlToImage,
            "publish_date": self.publishedAt,
        }
