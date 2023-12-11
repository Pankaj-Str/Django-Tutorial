# myapp/views.py
from django.shortcuts import render, redirect
from .forms import MyModelForm

def my_form(request):
    if request.method == 'POST':
        form = MyModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')  # Redirect to a success page
    else:
        form = MyModelForm()
    return render(request, 'myapp/my_form.html', {'form': form})

def success(request):
    return render(request, 'myapp/success.html')

