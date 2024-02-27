from django.urls import path
from . import views

urlpatterns = [
    path('', views.Emp_indexView.as_view(), name='emp-list'),
    path('detail/<int:pk>', views.EmpDetailView.as_view(), name='emp_detail'),
    path('search-blogs/', views.EmpSearchView.as_view(), name='search_emp')
]    