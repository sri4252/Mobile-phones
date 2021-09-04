from django.contrib import admin
from django.urls import path
from . import views 
from django.contrib.auth import views as auth_views

urlpatterns = [
   path('register/',views.register,name='register'),
   path('profile/',views.profile,name='profile'),
   path('staff/',views.staff,name='staff'),
   path('normal/',views.normal,name='normal'),
   path('success/',views.login_success,name='success'),
   path('login/',auth_views.LoginView.as_view(template_name='users/login.html'),name='login'),
   path('logout/',auth_views.LogoutView.as_view(template_name='users/logout.html'),name='logout'),
   
]