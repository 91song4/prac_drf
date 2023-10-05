from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

# 기존 장고 방식
def index(request):
    return HttpResponse('hello world!!')


# DRF 방식