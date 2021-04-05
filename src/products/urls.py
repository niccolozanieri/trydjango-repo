from django.contrib import admin
from django.urls import path
from .views import (
                            dynamic_lookup_view,
                            product_create_view,
                            product_delete_view,
                            products_list_view
                           )

urlpatterns = [
    path('create/', product_create_view, name='product-create'),
    path('', products_list_view, name='products-list'),
    path('<int:id>/', dynamic_lookup_view, name='product-detail'),
    path('<int:id>/delete/', product_delete_view, name='product-delete'),

]
