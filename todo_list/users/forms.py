from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import Profile


class RegisterForm(UserCreationForm):
    email = forms.EmailField(max_length=254)
    
    class Meta:
        model = User
        fields = ('username',  'email', 'password1', 'password2', )
        

# for profile update
class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['email']
        
class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['avatar']        