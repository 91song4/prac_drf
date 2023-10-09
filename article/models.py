from django.db import models

# Create your models here.


class Article(models.Model):
    title = models.CharField()
    content = models.TextField()
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
