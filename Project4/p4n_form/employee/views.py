from django.shortcuts import render
from .forms import EmployeeForm

def employee_form(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            # Redirect to a success page or do something else
    else:
        form = EmployeeForm()
    return render(request, 'employee_form.html', {'form': form})
