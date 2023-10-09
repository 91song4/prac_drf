from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view


# Create your views here.

# 기존 장고 방식
def index(request):
    return HttpResponse('hello world!!')


# DRF 방식
@api_view(['GET'])
def index_drf(request):
    return Response({'message': 'hello world drf!!'})
