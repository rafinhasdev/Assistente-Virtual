from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render

from .models import Usuarios


def login_view(request):
    return render(request, "registration/login.html")


def logout_view(request):
    logout(request)
    return redirect("login")
