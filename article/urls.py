from django.urls import path
from article import views

urlpatterns = [
    path('create/', views.create_article),
    path('read/', views.read_articles),
]
