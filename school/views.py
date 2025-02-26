# school/views.py

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login
from .models import User

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']
        user_type = request.POST['user_type']
        User.objects.create(username=username, password=password, email=email, user_type=user_type)
        return redirect('login')
    return render(request, 'register.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect('home')  # Redirect to home page
    return render(request, 'login.html')

def report_card(request):
    # Implement report card generation logic here
    pass
