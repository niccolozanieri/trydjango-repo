from django.shortcuts import render

# Create your views here.
from .models import Product

def product_detail_view(request): #do not call Product your view
    obj = Product.objects.get(id=1)
    context = {
        "object": obj
    }
    return render(request, "products/product_detail.html",context)
