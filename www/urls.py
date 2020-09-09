from django.urls import path

from www.views import index

urlpatterns = [
    path('', index, name='blog_index')
]
