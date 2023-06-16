from django.shortcuts import render
from django.contrib import messages
from .models import Blog

# Create your views here.

def blog(request):
	messages.success(request , "Welcome To The Blog Section")
	allPost = Blog.objects.all()[::-1]
	context = {'allPost':allPost}
	return render(request , 'blog/bloghome.html' , context)


def blogpost(request , slug):
	messages.success(request , "Welcome To The Blog Post")
	allPost = Blog.objects.filter(slug = slug).first()
	context = {'post':allPost}
	return render(request , 'blog/blogPost.html' , context)