from django.shortcuts import render

# Create your views here.
from www.models import Post


def index(request):
    posts = Post.objects.all()

    return render(request, 'index.html', {'content': posts})
