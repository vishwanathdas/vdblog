from django.shortcuts import render
from django.contrib import messages
from .models import Course

# Create your views here.

def course(request):
	messages.success(request , 'Welcome To The Premium Course Packegs')
	allPost = Course.objects.all()[::-1]
	context = {'allPost':allPost}
	return render(request , 'course/course.html' , context)


def coursepost(request , slug):
	allPost = Course.objects.filter(slug=slug).first()
	context = {'post':allPost}
	return render(request , 'course/coursepost.html' , context)	



