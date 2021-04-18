from django.shortcuts import get_object_or_404, render


# Create your views here.
from .models import Article
from .forms import CreateArticleForm
from django.views.generic import (
    ListView,
    DetailView
)


def articles_create_view(request):
    form = CreateArticleForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = CreateArticleForm()
    context = {
        'form': form
    }
    return render(request, "articles/articles_create.html", context)


class ArticlesListView(ListView):
    queryset = Article.objects.all()
    template_name = 'articles/articles_list.html'


class ArticlesDetailView(DetailView):
    template_name = 'articles/articles_detail.html'

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Article, id=id_)
