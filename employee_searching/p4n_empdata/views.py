from django.shortcuts import render
from .models import EmpData
from django.views.generic import ListView , DetailView

class Emp_indexView(ListView):
    model = EmpData
    template_name = 'employee.html'
    queryset = EmpData.objects.all()
    context_object_name = 'emp'

class EmpDetailView(DetailView):
    model = EmpData
    context_object_name = 'emp'
    template_name = 'emp_detail.html'   

class EmpSearchView(ListView):
    model = EmpData
    template_name = 'employee.html'
    context_object_name = 'emp'

    def get_queryset(self):
        query = self.request.GET.get('q')
        return EmpData.objects.filter(title__icontains=query).order_by('-created_at')    