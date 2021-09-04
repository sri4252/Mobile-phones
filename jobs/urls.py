from django.urls import path
from . import views

urlpatterns = [
	path('home',views.home,name='home'),
	path('contact',views.contact,name='contact'),
	path('job_details/<int:pk>',views.job_details,name='details'),
    path('',views.job_list,name = 'list'),
      
]