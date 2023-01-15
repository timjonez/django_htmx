from django.shortcuts import render

def blog_list_view(request):
    return render(request, 'blog/blog_list.html')
