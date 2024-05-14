from django.shortcuts import render, redirect
from django.views.generic.base import View
from .models import Post, Comments, Category
from .form import comment_form
from .filter import post_filter
# Create your views here.

# View - functional based view
# Class based view

class PostView(View):
    def get(self, request):
        posts = Post.objects.all()
        return render(request, 'blog.html', {'posts':posts})

def post_detail(request, id):
    post = Post.objects.get(id=id)
    return render(request, 'blog_detail.html', {'post':post})


def AddComments(request, id):
    form = comment_form(request.POST)
    if form.is_valid():
        form = form.save(commit=False)
        form.post_id = id
        form.save()
    return redirect(f'/{id}')

def get_categories(request):
    categories = Category.objects.all()
    return render(request, 'category.html', {'categories':categories})

def post_list(request):
    filter = post_filter(request.GET, queryset=Post.objects.all())
    return render(request, 'blog.html', {'filter':filter})