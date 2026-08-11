from django.shortcuts import render
from django.http import HttpResponse

from .forms import EmployeeForm
# Create your views here.

from .models import UserProfile

def Home(request):
    profiles = UserProfile.objects.all()
    return render(request,"home.html",{'profiles': profiles})


def employee_form(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            # Redirect to a success page or do something else
    else:
        form = EmployeeForm()
    return render(request, 'employeeform.html', {'form': form})