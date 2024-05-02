from django.shortcuts import render, redirect
from django.views.generic.base import View
from .models import Post
from .form import CommentsForm
# Create your views here.

# View - functional based view
# Class based view

class PostView(View):
    def get(self, request):
        posts = Post.objects.all()
        return render(request, 'blog.html', {'posts':posts})

class PostDetail(View):
    def get(self, request, id):
        post = Post.objects.get(id=id)
        return render(request, 'blog_detail.html', {'post':post})


class AddComment(View):
    def post(self, request, id):
        form = CommentsForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.post_id = id
            form.save()
        return redirect(f'/{id}')