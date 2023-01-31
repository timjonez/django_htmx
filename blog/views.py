from django.shortcuts import render
from .models import Post


def blog_list_view(request):
    posts = Post.objects.all()
    return render(request, 'blog/blog_list.html', {"posts": posts})

def blog_detail_view(request):
    post = Post.objects.last()
    return render(request, 'blog/post_detail.html', {"post": post})
