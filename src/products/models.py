from django.db import models
from django.urls import reverse

# Create your models here.


class Product(models.Model):
    title = models.CharField(max_length=30, null=False, blank=False)
    price = models.DecimalField(max_digits=100, decimal_places=2, null=False, blank=False)
    description = models.TextField(max_length=200, blank=True)

    def get_absolute_url(self):
        return reverse("product-detail", kwargs={"id":self.id})
