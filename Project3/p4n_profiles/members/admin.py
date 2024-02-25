from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import UserProfile

admin.site.register(UserProfile)
