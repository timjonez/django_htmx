from django.urls import path
from . import views

urlpatterns = [
    path('', views.blog_list_view, name='post-list'),
    path('post/', views.blog_detail_view, name='post-detail'),
]
