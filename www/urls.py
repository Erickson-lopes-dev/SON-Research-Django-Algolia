from django.urls import path

from www.views import index, show

urlpatterns = [
    path('', index, name='index'),
    path('<int:id>', show, name='show')
]
