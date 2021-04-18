from django.shortcuts import get_object_or_404, render
from .forms import CreateArticleForm
# Create your views here.


def articles_create_view(request):
    form = CreateArticleForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = CreateArticleForm()
    context = {
        'form': form
    }
    return render(request, "blog/articles_create.html", context)