from django.shortcuts import render
from django.views.generic.base import View
from .models import Post

# Create your views here.

# View - functional based view
# Class based view

class PostView(View):
    def get(self, request):
        posts = Post.objects.all()
        return render(request, 'blog.html', {'posts':posts})