# Third Party Imports
from django.conf.urls import url
from django.contrib.auth import views

# Local
from reachlocalnews.articles import views

urlpatterns = [
    url(r'articles', 
        views.ArticlesView.as_view(), name='articles'),
    url(r'json', 
    	views.ArticlesJSON.as_view(), name='show_articles_json'),
]
