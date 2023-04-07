from django.shortcuts import render, get_object_or_404, redirect
from rest_framework.decorators import api_view
from rest_framework.response import Response

from Blog_article.models.article import Article
from Blog_article.serializers import ArticleSerializer


@api_view(['GET'])
def article_list(request):
    articles = Article.objects.filter(is_delete=False).select_related('author')
    serializer = ArticleSerializer(articles, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def article_detail(request, article_id):
    article = get_object_or_404(Article.objects.select_related('author'), id=article_id, is_delete=False)
    serializer = ArticleSerializer(article)
    return Response(serializer.data)


@api_view(['POST'])
def article_create(request):
    serializer = ArticleSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)


@api_view(['PUT'])
def article_update(request, article_id):
    article = get_object_or_404(Article.objects.select_related('author'), id=article_id, is_delete=False)
    serializer = ArticleSerializer(instance=article, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=400)


@api_view(['DELETE'])
def article_delete(request, article_id):
    article = get_object_or_404(Article.objects.select_related('author'), id=article_id, is_delete=False)
    article.is_delete = True
    article.save()
    return Response(status=204)