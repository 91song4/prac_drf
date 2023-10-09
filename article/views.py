from django.shortcuts import get_object_or_404
from django.utils import timezone
from rest_framework.decorators import api_view
from rest_framework.response import Response
from article.models import Article

from article.serializers import ArticleSerializer
# Create your views here.


@api_view(['post'])
def create_article(req):
    serializer = ArticleSerializer(data=req.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)

    return Response(serializer.errors, status=400)


@api_view(['get'])
def read_articles(req):
    articles = Article.objects.all().filter(
        delete_date=None).order_by('-create_date')
    serializer = ArticleSerializer(articles, many=True)

    return Response(serializer.data, status=200)


@api_view(['get'])
def read_article(req, article_id):
    articles = get_object_or_404(Article, pk=article_id)
    serializer = ArticleSerializer(articles)

    return Response(serializer.data, status=200)


@api_view(['patch'])
def update_article(req, article_id):
    article = get_object_or_404(Article, pk=article_id)
    serializer = ArticleSerializer(article, data=req.data, partial=True)

    if serializer.is_valid():
        serializer.save()

        return Response(serializer.data, status=200)

    return Response(serializer.errors, status=400)


@api_view(['delete'])
def soft_delete_article(req, article_id):
    article = get_object_or_404(Article, pk=article_id)
    article.delete_date = timezone.now()
    article.save()

    return Response(status=200)


@api_view(['delete'])
def destroy_article(req, article_id):
    article = get_object_or_404(Article, pk=article_id)
    article.delete()

    return Response(status=200)
