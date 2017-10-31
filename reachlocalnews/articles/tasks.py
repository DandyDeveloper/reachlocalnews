# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.conf import settings
import requests
import re

# Local
from reachlocalnews.celery import app
from .serializer import ArticleSerializer, SourcesSerializer
from .models import Article, Source


app.conf.beat_schedule ={
    'get-sources-every-10-seconds': {
        'task': 'reachlocalnews.articles.tasks.get_sources',
        'schedule': 10.0,
    },
    'get-articles-every-minute': {
        'task': 'reachlocalnews.articles.tasks.get_articles',
        'schedule': 60.0
    },
}

@app.task
def get_sources():
    ''' Gets sources from newsapi.org. New sources are checked 
        and added if not in database. Task is called every 10 seconds
        by Celery Beat Schedule defined at top of file.

    '''
    r = requests.get(
            'https://newsapi.org/v1/sources?language=en'
        )
    sources = r.json()

    for source in sources['sources']: 
        if Sources.objects.filter(source_id=source['id']):
            pass
        else:
            valid_data = {
                'source_id': source['id'],
                'name': source['name']
            }
            serialized_data = SourcesSerializer(data=valid_data)

            if serialized_data.is_valid():
                SourcesSerializer.save(serialized_data)

@app.task
def get_articles():
    ''' Gets articles from sources saved in database via newsapi. 
        Task is called via Celery Beat schedule every 30 seconds
        defined at top of file. Poplulates the Articles model.
    '''
    is_url = re.compile(r'\s?(?:http)s?://')
    name_in_url = re.compile(r'/.*/(.*)/')
    source_list = Sources.objects.filter()

    for source in source_list:
        r = requests.get(
               'https://newsapi.org/v1/articles?source=' + source.source_id + '&sort-By=latest&apiKey=' + settings.API_KEY
            )
        articles = r.json()

        for article in articles['articles']:
            # If article exists. Ignore.
            if Article.objects.filter(url=article['url']):
                pass
            else:
                # Add source to article Object
                article['source'] = articles['source']

                # Block to support different article API problems
                # Is no author given. Populate with source.
                if article['author'] is None:
                    article['author'] = article['source']
                # If multiple articles. Add both to article listing.
                elif len(article['author'].split(',')) >= 2:
                    authors = []
                    for author in article['author'].strip().split(','):
                        if re.match(is_url, author):
                            name = re.search(name_in_url, author)
                            authors.append(name.group(1))
                        else:
                            authors.append(author)
                    article['author'] = ' '.join(authors)
                # If URL... Convert to name
                elif re.match(is_url, article['author']):
                    name = re.search(name_in_url, article['author']).group(1)
                    article['author'] = name

                serialized_data = ArticleSerializer(data=article)

                if serialized_data.is_valid():
                    ArticleSerializer.save(serialized_data)
                else:
                    # Raises errors in DEBUG.
                    print(serialized_data.errors)
