from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group


def login_view(request):

    if request.user.is_authenticated:
        return redirect("dashboard")

    if request.method == "POST":

        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:

            login(request, user)

            if user.is_superuser:
                return redirect("dashboard")

            elif user.groups.filter(name="Teacher").exists():
                return redirect("teacher_dashboard")

            elif user.groups.filter(name="Student").exists():
                return redirect("student_dashboard")

            else:
                return redirect("dashboard")

        else:
            messages.error(request, "Invalid Username or Password")

    return render(request, "accounts/login.html")


@login_required
def logout_view(request):

    logout(request)

    return redirect("login")


@login_required
def profile(request):

    return render(request, "accounts/profile.html")


@login_required
def change_password(request):

    return render(request, "accounts/change_password.html")