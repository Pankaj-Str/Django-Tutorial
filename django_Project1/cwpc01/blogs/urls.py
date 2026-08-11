from django.urls import path
from . import views

urlpatterns = [
     path("", views.Home,name="home"),
     path('form/', views.employee_form, name='employee_form')
]
