from datetime import date
from django.db import models


class stu(models.Model):
	first_name = models.CharField(max_length = 40, null = True)
	last_name = models.CharField(max_length = 40, null = True)
	dob = models.IntegerField(null = True)
	img = models.ImageField(null = True)
	
	def __str__(self):
		return "{}".format(self.id)
class mark(models.Model):
	subject =models.CharField(max_length = 40,null = True)
	mark = models.IntegerField(null = True)
	created_date = models.DateTimeField(auto_now_add = True)
	date_modified = models.DateTimeField(auto_now=True)
	student = models.ForeignKey(stu, on_delete = models.CASCADE)
	updated_by = models.CharField(max_length=20, null = True)
	created_by = models.CharField(max_length=20, null = True)
	def __str__(self):
		return "{} {} {} {} {} ".format(self.subject,self.mark,self.created_date,self.date_modified,self.student)
# Create your models here.	img = models.ImageField()
