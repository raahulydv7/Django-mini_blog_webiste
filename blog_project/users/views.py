from django.shortcuts import render, redirect
from .forms import (
    CustomAuthenticationForm,
    CustomUserCreationForm,
    CustomUserProfileForm,
)
from .models import UserProfile
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import login, logout


# Create your views here.
def home(request):
    user_profile = UserProfile.objects.filter(user=request.user).first()
    print(user_profile)
    return render(
        request,
        "users/home.html",
        {
            "user_profile": user_profile,
        },
    )


def user_register_view(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            username = form.cleaned_data.get("username")
            messages.success(
                request, f"Account created for {username}! You are loged in."
            )
            return redirect("home")
        else:
            messages.error(request, "Account Can't created")
            return redirect("register")
    else:
        form = CustomUserCreationForm()
    return render(request, "users/register.html", {"form": form})


def User_login_view(request):
    if request.method == "POST":
        form = CustomAuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, f"Welcome {user.username}")
            return redirect("home")
        else:
            messages.error(request, "Invalid username or password")
            return redirect("login")
    else:
        form = CustomAuthenticationForm()
    return render(request, "users/login.html", {"form": form})


@login_required
def User_profile_view(request):
    user_profile, created = UserProfile.objects.get_or_create(user=request.user)
    if request.method == "POST":
        form = CustomUserProfileForm(request.POST, request.FILES, instance=user_profile)
        if form.is_valid():
            form.save()
            messages.success(request, f"Profile updated successfully.")
            return redirect("home")
        else:
            messages.error(request, "Profile can't updated")
            return redirect("profile")
    else:
        form = CustomUserProfileForm(instance=user_profile)
    return render(request, "users/profile.html", {"form": form})


def user_logout_view(request):
    logout(request)
    messages.success(request, "You have been logged out.")
    return redirect("login")
