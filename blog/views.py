from django.shortcuts import render
from .models import Post


def blog_list_view(request):
    posts = Post.objects.all()
    return render(request, 'blog/blog_list.html', {"posts": posts})
