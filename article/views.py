from rest_framework.decorators import api_view
from rest_framework.response import Response

from article.serializers import ArticleSerializer
# Create your views here.


@api_view(['post'])
def create_article(req):
    serializer = ArticleSerializer(data=req.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)

    return Response(serializer.errors, status=400)
