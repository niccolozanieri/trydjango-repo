from django.db import models

# Create your models here.


class Article(models.Model):
    title = models.CharField(max_length=40, null= False, blank= False)
    text = models.TextField(null= False, blank= False)
    author = models.CharField(max_length=40, null= False, blank= True)
    date = models.DateField(auto_now_add= True)
