from django.shortcuts import render
from .models import User
from django.shortcuts import redirect

import hashlib

def register(request):
    if request.session.get('user'):
        return redirect('/home/')
    status = request.GET.get('status')
    return render(request, 'register.html', {'status': status})

def login(request):
    if request.session.get('user'):
        return redirect('/home/')
    status = request.GET.get('status')
    return render(request, 'login.html', {'status': status})

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

def check_login(request):
    email = request.POST.get('email')
    password = request.POST.get('password')

    password = hashlib.sha256(password.encode()).hexdigest()

    user_exists = User.objects.filter(email = email).filter(password = password)

    if len(user_exists) == 0:
        return redirect('/auth/login/?status=1')
    request.session['user'] = user_exists[0].id   
    return redirect('/home/')

def logout(request):
    request.session.flush()
    return redirect('/home/')
