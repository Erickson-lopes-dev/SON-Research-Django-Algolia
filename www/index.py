from algoliasearch_django import AlgoliaIndex
from algoliasearch_django.decorators import register

from .models import Post


@register(Post)
class PostIndex(AlgoliaIndex):
    # campos
    fields = ('id', 'title', 'content', 'createt_at')
    # pesquisar por
    settings = {'searchableAttributes': ['title', 'content']}
    # quando criar index do algolia este sera o index
    index_name = 'blog_posts'






