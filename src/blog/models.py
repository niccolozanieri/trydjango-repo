from django.db import models

# Create your models here.


class Article(models.Model):
    author = models.CharField(max_length=40, default='Anonymous')
    text = models.TextField(blank=True, null=True)
    title = models.CharField(max_length=50)
    likes = models.PositiveIntegerField(default=0)
    dislikes = models.PositiveIntegerField(default=0)



