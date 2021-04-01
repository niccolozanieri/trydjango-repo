from django.shortcuts import render

# Create your views here.
from .models import Product
from .forms import ProductForm






# def product_create_view(request):
#     print(request.POST)
#     print(request.POST.get('title'))
#     return render(request, "products/product_create.html", {})

def product_create_view(request):
    form = ProductForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = ProductForm()
    context = {
        'form': form
    }
    return render(request, "products/product_create.html", context)

def product_detail_view(request): #do not call Product your view
    obj = Product.objects.get(id=1)
    context = {
        "object": obj
    }
    return render(request, "products/product_detail.html",context)
