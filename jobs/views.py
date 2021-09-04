from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
from .models import Job

# Create your views here.
def home(request):
	return render(request,'home.html',{})

def contact(request):
	if request.method == 'POST':
		firstname = request.POST['firstname']
		lastname = request.POST['lastname']
		country = request.POST['country']
		subject = request.POST['subject']
		send_mail('Contact Form',
			"firstname: "+str(firstname)+"\n"
	        "lastname:"+str(lastname)+"\n"
	        "country:"+str(country)+"\n"
	        "subject :"+ str(subject),
		 settings.EMAIL_HOST_USER,
		 ['mkumarf4u@gmail.com'], 
		 fail_silently=False)
	return render(request,'contact.html')	

def job_details(request,pk):
	jl = Job.objects.filter(pk=pk)
	context = {
	'jl':jl
	}
	return render(request,'details.html',context)
		
def job_list(request):
	jl = Job.objects.all()
	context = {
	'jl':jl
	}
	return render(request,'list.html',context)