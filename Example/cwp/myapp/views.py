# myapp/views.py
from django.shortcuts import render, redirect
from .forms import MyModelForm

def my_view(request):
    if request.method == 'POST':
        form = MyModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')  # Create a success.html template for the success page
    else:
        form = MyModelForm()

    return render(request, 'myapp/form.html', {'form': form})

def success_view(request):
    return render(request, 'myapp/success.html')