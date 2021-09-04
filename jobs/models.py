from django.db import models
from datetime import datetime

# Create your models here.
class Job(models.Model):
	title = models.CharField(max_length=100)
	skills = models.CharField(max_length=100)
	company = models.CharField(max_length=100)
	location = models.CharField(max_length=100)
	jobtype = models.CharField(max_length=100)
	posteddate = models.DateTimeField(auto_now_add=True)
	aboutjob = models.CharField(max_length=100)
	image = models.FileField(upload_to ='media' )

	def __str__(self):
		return self.skills
		