from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

from .models import UserProfile

def Home(request):
    profiles = UserProfile.objects.all()
    return render(request,"home.html",{'profiles': profiles})


def aboutus(request):
    return HttpResponse("welcome to About US")