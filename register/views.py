from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from .forms import RegisterForm

# Create your views here.
def register(resp):
    if resp.method == "POST":
        form = RegisterForm(resp.POST)
        if form.is_valid():
            form.save()
        
        return redirect('index')
    else:
        form = RegisterForm()    
    return render(resp, "register/register.html", {"form":form})
