from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .models import UserProfile

def display_profiles(request):
    profiles = UserProfile.objects.all()
    return render(request, 'members/profile_list.html', {'profiles': profiles})
