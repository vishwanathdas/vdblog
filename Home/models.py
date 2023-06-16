from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
class Contact(models.Model):
	sno = models.AutoField(primary_key = True)
	name = models.CharField(max_length = 30)
	phone = models.CharField(max_length = 10)
	email = models.CharField(max_length = 55)
	msg = RichTextField(blank = True , null = True)
	time = models.DateTimeField(auto_now_add = True , blank = True)

	def __str__(self):
		return self.name

		
class About(models.Model):
	sno = models.AutoField(primary_key = True)
	title = models.CharField(max_length = 100)
	content = RichTextField(blank = True , null = True)
	time = models.DateTimeField(auto_now_add = True , blank = True)

	def __str__(self):
		return self.title       


class Privacy(models.Model):
	sno = models.AutoField(primary_key = True)
	title = models.CharField(max_length = 100)
	content = RichTextField(blank = True , null = True)
	time = models.DateTimeField(auto_now_add = True , blank = True)

	def __str__(self):
		return self.title   

class ContactService(models.Model):
	sno = models.AutoField(primary_key = True)
	phone = models.CharField(max_length = 15)
	email = models.CharField(max_length = 30)

	def __str__(self):
		return self.phone

class HeadOffice(models.Model):
	sno = models.AutoField(primary_key = True)
	company_name = models.CharField(max_length = 20)
	Street = models.CharField(max_length = 100)
	pincode_city_country = models.CharField(max_length = 75)
	phone = models.CharField(max_length = 15)
	email = models.CharField(max_length = 30)

	def __str__(self):
		return self.company_name

class IndiaOffice(models.Model):
	sno = models.AutoField(primary_key = True)
	company_name = models.CharField(max_length = 20)
	Street = models.CharField(max_length = 100)
	pincode_city_country = models.CharField(max_length = 75)
	phone = models.CharField(max_length = 15)
	email = models.CharField(max_length = 30)

	def __str__(self):
		return self.company_name



