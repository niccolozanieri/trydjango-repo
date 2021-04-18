from django.contrib import admin
from django.urls import include, path
from .views import (
    articles_create_view,
    ArticlesListView,
    ArticlesDetailView
)


app_name = 'articles'
urlpatterns = [
    path('create/', articles_create_view, name="articles-create"),
    path('articles/', ArticlesListView.as_view(), name="articles-list"),
    path('articles/<int:id>/', ArticlesDetailView.as_view(), name="articles-detail")
]
