from django.shortcuts import render, redirect, get_object_or_404
from .forms import RegisterForm, UserForm, ProfileForm
from django.contrib.auth.models import User

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

def profile_detail(request, pk):
    user = get_object_or_404(User, pk=pk)
    return render(request, 'register/profile_detail.html', {'user': user})

def profile_edit(request, pk):
    user = get_object_or_404(User, pk=pk)
    if request.method == 'POST':
        user_form = UserForm(request.Post, instance=request.user)
        profile_form = ProfileForm(request.Post, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect('profile_detail', pk=user.pk)
    else:
        user_form = UserForm(instance=request.user)
        profile_form = ProfileForm(instance=request.user.profile)    
    return render(request, 'register/profile_edit.html', {'user_form': user_form, 'profile_form': profile_form})