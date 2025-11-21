from django.contrib.auth import logout
from django.shortcuts import redirect, render


def login_view(request):
    return render(request, "registration/login.html")


def logout_view(request):
    logout(request)
    return redirect("login")
