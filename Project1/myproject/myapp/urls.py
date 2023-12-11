# myapp/urls.py
from django.urls import path
from .views import my_form, success

urlpatterns = [
    path('form/', my_form, name='my_form'),
    path('success/', success, name='success'),
]
