from rest_framework import serializers
from .models import Article, Sources

class SourcesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sources
        fields = ('source_id', 'name')

class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = '__all__'
