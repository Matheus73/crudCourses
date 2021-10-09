from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('check_register/', views.check_register, name='check_register'),
    path('check_login/', views.check_login, name='check_login'),
    path('logout/', views.logout, name='logout')
]
