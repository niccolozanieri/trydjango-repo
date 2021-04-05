from django.db import models
from django.urls import reverse

# Create your models here.


class Article(models.Model):
    title = models.CharField(max_length=40, null= False, blank= False)
    text = models.TextField(null= False, blank= False)
    author = models.CharField(max_length=40, null= False, blank= True)
    date = models.DateField(auto_now_add= True)

    def get_absolute_url(self, *args, **kwargs):
        return reverse
