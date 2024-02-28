from django.shortcuts import render
from .forms import EmployeeSearchForm
from .models import Employee

def search_employee(request):
    if request.method == 'GET':
        form = EmployeeSearchForm(request.GET)
        if form.is_valid():
            search_query = form.cleaned_data['search_query']
            employees = Employee.objects.filter(name__icontains=search_query)
            return render(request, 'employee_directory/search_results.html', {'employees': employees, 'search_query': search_query})
    else:
        form = EmployeeSearchForm()
    return render(request, 'employee_directory/search_form.html', {'form': form})
