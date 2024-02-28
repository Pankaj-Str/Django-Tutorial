from django.urls import path
from .views import search_employee

urlpatterns = [
    path('', search_employee, name='search_employee'),
]
