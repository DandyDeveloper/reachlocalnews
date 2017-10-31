# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.views.generic import TemplateView, View
from django.http import JsonResponse

# Local
from .models import Article


class ArticlesView(TemplateView):
    ''' Display list of articles in articles.html template '''
    template_name = 'articles.html'
    
    def get_context_data(self, **kwargs):
        context = super(ArticlesView, self).get_context_data(**kwargs)
        context['latest_articles'] = Article.objects.all().order_by('-id')[:20]
        
        return context


class ArticlesJSON(View):
    ''' Display last 100 new articles imported from API '''
    def get(self, request): 
        articles = Article.objects.all().order_by('-id')[:100]
        articles_dict = [ article.as_dict() for article in articles ]

        return JsonResponse(articles_dict, safe=False)
