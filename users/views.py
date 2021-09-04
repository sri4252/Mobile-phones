from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
# from posts.models import post
# from posts.forms import postForm
from .forms import UserRegisterForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required

def register(request):
	if request.method == 'POST':
		form = UserRegisterForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data.get('username')
			messages.success(request,('Account created for '+str(username)))
			return redirect('/')
	else:
		form = UserRegisterForm()
	return render(request,'users/register.html',{'form':form})

@login_required
def profile(request):
	return render(request,'users/profile.html')

@login_required
def login_success(request):
    if request.user.is_staff:
        return HttpResponseRedirect('/')
    else:
        return HttpResponseRedirect('/')


@staff_member_required
def staff(request):
	return render(request,'staff.html')

	
@login_required
def normal(request):
	return render(request,'normal.html')