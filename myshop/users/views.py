from typing import ContextManager
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login
from .forms import CustomUserChangeForm, CustomUserCreationForm, ProfileUpdateForm
from django.contrib.auth.decorators import login_required


def register(request):
    
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect('/')
        
    else:
        form = CustomUserCreationForm()

    context = {
        'form': form
    }

    return render(request, 'users/register.html', context)

@login_required
def profile(request):
    return f"Hello {request.user.username}"


@login_required
def update_profile(request):
    if request.method == "POST":
        # u_form = CustomUserChangeForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, instance=request.user)

        if p_form.is_valid():
            # u_form.save()
            p_form.save()
            return redirect('profile')
        
    else:
        # u_form = CustomUserChangeForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user)
    
    context = {
        # 'u_form': u_form,
        'p_form': p_form
    }
    
    return render(request, 'users/profile.html', context)