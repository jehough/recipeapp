from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from register.models import Profile


class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username", 'email', 'first_name', 'last_name', "password1", "password2"]

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')
        
class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('bio', 'location', 'birth_date')
