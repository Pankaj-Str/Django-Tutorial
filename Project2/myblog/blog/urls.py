# blog/urls.py
from django.urls import path
from .views import create_post, show_posts

urlpatterns = [
    path('create/', create_post, name='create_post'),
    path('show/', show_posts, name='show_posts'),
]
