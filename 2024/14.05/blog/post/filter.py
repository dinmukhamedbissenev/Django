import django_filters
from .models import Post

class post_filter(django_filters.FilterSet):
    class Meta:
        model = Post
        fields = ['category']