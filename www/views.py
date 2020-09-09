from django.shortcuts import render

# Create your views here.
from www.models import Post


def index(request):
    posts = Post.objects.all()[:10]

    return render(request, 'index.html', {'posts': posts})


def show(request, id):
    posts = Post.objects.get(pk=id)
    return render(request, 'show.html', {'post': posts})
