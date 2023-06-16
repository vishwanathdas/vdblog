from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.

class Blog(models.Model):
	sno = models.AutoField(primary_key = True)
	title = models.CharField(max_length = 255)
	content = RichTextField(blank = True , null = True)
	author = models.CharField(max_length = 30)
	img = models.ImageField(upload_to='images/')
	time = models.DateTimeField(blank = True)
	slug = models.CharField(max_length = 255)

	def __str__(self):
		return self.title