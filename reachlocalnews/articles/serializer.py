from rest_framework import serializers
from .models import Article, Source


class SourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Source
        fields = ('source_id', 'name')


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = '__all__'
