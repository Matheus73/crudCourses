from django.shortcuts import render
from .models import User
from django.shortcuts import redirect

import hashlib

def register(request):
    status = request.GET.get('status')
    return render(request, 'register.html', {'status': status})

def login(request):
    return render(request, 'login.html')

def check_register(request):
    name = request.POST.get('name')
    email = request.POST.get('email')
    password = request.POST.get('password')
    
    user_exists = User.objects.filter(email = email)

    if len(user_exists) > 0:
        return redirect('/auth/register/?status=1')
    
    if len(name.strip()) == 0 or len(email.strip()) == 0:
        return redirect('/auth/register/?status=2')
    
    if len(password) < 8:
        return redirect('/auth/register/?status=3')
    
    try:
        password = hashlib.sha256(password.encode()).hexdigest()
        user = User(name = name,
                       email = email,
                       password = password)
        user.save()
        return redirect('/auth/register/?status=0')
    except:
        return redirect('/auth/register/?status=4')
