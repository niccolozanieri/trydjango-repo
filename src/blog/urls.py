from django.contrib import admin
from django.urls import include, path
from .views import (
    articles_create_view
)


app_name = 'blog'
urlpatterns = [
    path('create/', articles_create_view, name="articles-create"),
]
