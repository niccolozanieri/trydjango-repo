from django.shortcuts import render


# Create your views here.

def home_view(request, *args, **kwargs):
    return render(request, "home.html")


def about_view(request, *args, **kwargs):
    my_context = {
        "my_list": [1, 2, 3, 4]
    }
    return render(request, "about.html", my_context)
