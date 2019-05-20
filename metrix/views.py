from django.shortcuts import render
from django.conf import settings
from rest_framework import generics, viewsets, mixins
from rest_framework.response import Response
from django.contrib.auth.models import User, Group
from rest_framework import status
from . models import Article
from . import serializers
from rest_framework.authentication import TokenAuthentication
from django.contrib.auth.tokens import default_token_generator
from rest_framework.authtoken.models import Token
# Create your views here.


class ArticleView(generics.ListAPIView):
    """docstring for ProjectView"""
    model = Article
    serializer_class = serializers.ArticleSerializer
    authentication_classes = (TokenAuthentication,)

    def post(self, request):
        auth_user = User.objects.get(id=request.data['user'])
        author = auth_user
        title = request.data['title']
        content = request.data['content']
        a = Article(author=author, title=title, content=content)
        a.save()
        # For sending response, we use the below line
        art_serializer = self.serializer_class(a)
        print "Article Data Inserted Successfully"
        return Response(art_serializer.data, status=status.HTTP_200_OK)

    def get_queryset(self):
        return Article.objects.all()

    def get(self, request):
        articles = self.get_queryset()
        art_serializer = self.serializer_class(articles)
        return Response(art_serializer.data, status=status.HTTP_200_OK)

    def put(self, request, *args, **kars):
        update_articles = Article.objects.get(id=kars['pk'])
        update_articles.title = request.data['title']
        update_articles.save()
        art_serializer = self.serializer_class(update_articles)
        return Response(art_serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, **kars):
        update_articles = Article.objects.get(id=kars['pk'])
        update_articles.delete()
        return Response({'success': 'Deleted Succesffully'}, status=status.HTTP_200_OK)
