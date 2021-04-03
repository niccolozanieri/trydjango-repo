from django.shortcuts import get_object_or_404, redirect, render

# Create your views here.
from .models import Product
from .forms import ProductForm, RawProductForm


def product_create_view(request): # we're using this because it's clearer
    form = ProductForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = ProductForm()
    context = {
        'form': form
    }
    return render(request, "products/product_create.html", context)


def product_delete_view(request, id):
    obj = Product.objects.get(id=id)
    if request.method == "POST":
        obj.delete()
        return redirect("../../")

    context = {
        'object': obj
    }
    return render(request, "products/product_delete.html", )

def products_list_view(request):
    queryset = Product.objects.all()
    context = {
        'objects_list': queryset
    }
    return render(request, "products/products_list.html", context)


def dynamic_lookup_view(request, id): #do not call Product your view
    # obj = Product.objects.get(id= my_id)
    obj = get_object_or_404(Product, id= id)
    context = {
        "object": obj
    }
    return render(request, "products/product_detail.html",context)

# def product_create_view(request):
#     my_form = RawProductForm()
#     if request.method == "POST":
#         my_form = RawProductForm(request.POST)
#         if my_form.is_valid():
#             Product.objects.create(**my_form.cleaned_data)
#             print(request.POST)
#             my_form = RawProductForm()
#         else:
#             print(my_form.errors)
#
#     context = {
#         "form": my_form,
#     }
#     return render(request, "products/product_create.html", context)



# def product_create_view(request):
#     print(request.POST)
#     print(request.POST.get('title'))
#     return render(request, "products/product_create.html", {})
