from rest_framework import serializers
from . models import Article
from django.contrib.auth.models import User, Group


class AuthSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"


class ArticleSerializer(serializers.ModelSerializer):
    author = AuthSerializer(many=False, read_only=True)

    class Meta:
        model = Article
        fields = "__all__"
