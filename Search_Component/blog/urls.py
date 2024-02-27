from django.urls import path
from . import views

urlpatterns = [
    path('', views.PostIndexView.as_view(), name='post-list'),
    path('detail/<int:pk>', views.PostDetailView.as_view(), name='post_detail'),
    path('search-blogs/', views.BlogSearchView.as_view(), name='search_blogs')
]
