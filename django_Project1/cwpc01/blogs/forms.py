from django import forms
from .models import UserProfile

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['first_name', 'last_name', 'email', 'phone_number']