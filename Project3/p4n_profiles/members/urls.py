from django.urls import path
from .views import display_profiles

urlpatterns = [
    path('profiles/', display_profiles, name='profile_list'),
]
