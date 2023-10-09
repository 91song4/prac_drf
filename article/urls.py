from django.urls import path
from article import views

urlpatterns = [
    path('create/', views.create_article),
    path('read/', views.read_articles),
    path('read/<int:article_id>/', views.read_article),
    path('update/<int:article_id>/', views.update_article),
    path('soft-delete/<int:article_id>/', views.soft_delete_article),
    path('destroy/<int:article_id>/', views.destroy_article),
]
