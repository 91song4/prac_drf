from django.db import models

# Create your models here.


class Article(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    delete_date = models.DateTimeField(null=True, default=None)
