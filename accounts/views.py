from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Usuarios

def login_view(request):
    return render(request, 'registration/login.html')

def logout_view(request):
    logout(request)
    messages.info(request, "Saindo!")
    return redirect('login')

def callback_view(request):
    return redirect('home')