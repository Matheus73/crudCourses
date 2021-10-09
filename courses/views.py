from django.shortcuts import render
from .models import Courses, Classes
from django.shortcuts import redirect

def home(request):
    if request.session.get('user'):
        courses = Courses.objects.all()
        request_usuario = request.session.get('user')
        return render(request, 'home.html', {'courses': courses, 'request_usuario': request_usuario})
    else:
        return redirect('/auth/login/?status=2')

def course(request, id):
    if request.session.get('user'):
        classes = Classes.objects.filter(course = id)
        request_usuario = request.session.get('user')
        return render(request, 'course.html', {'classes': classes, 'request_usuario': request_usuario})
    else:
        return redirect('/auth/login/?status=2')
