# myapp/urls.py
from django.urls import path
from .views import my_view , success_view

urlpatterns = [
    path('form/', my_view, name='form'),
    path('success/', success_view, name='success'),
]
