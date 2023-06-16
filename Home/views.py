from django.shortcuts import render , redirect
from django.contrib import messages
from Home.models import Contact , About , Privacy , HeadOffice , IndiaOffice , ContactService
from Course.models import Course
# Create your views here.
def home(request):
	messages.success(request , "Welcome To The VdBlog")
	allPosts = Course.objects.all()[::-1]
	allPosts = allPosts[:3]
	context = {'allPost':allPosts}
	return render(request , 'home/home.html',context)

def contact(request):
	messages.success(request, "Welcome To The Contact Page")
	# HeadOffice Area 
	Headpost = HeadOffice.objects.all().first()
	context = {'Headpost':Headpost}
	# return redirect(request , 'home/contact.html' , context)
	# return render(request , 'home/contact.html' , conteat)
	# # IndiaOffice Area
	# Indiapost = IndiaOffice.objects.all().first()
	# return render(request , 'home/contact.html' , conteet)
	# # ContactService Area
	# Contactpost = ContactService.objects.all().first()
	# return render(request , 'home/contact.html' , content)
	# context = {'HeadPost':Headpost,'allPostc':Contactpost,'allPosti':Indiapost}

	if request.method == 'POST':
		name = request.POST['name']
		phone = request.POST['phone']
		email = request.POST['email']
		content = request.POST['text']

		if len(name) < 5 or len(email) < 10 or len(phone) < 10 or len(content) < 10:
			messages.warning(request , "Fill Contact Form Properly")
		else:
			contact = Contact(name = name , email = email , phone = phone , msg = content)
			contact.save()
			messages.success(request , "Form Successfully Submit ")
	return render(request , 'home/contact.html')

def about(request):
	# messages.success(request , "Welcome To The About Us ")
	allPosts = About.objects.all().first()
	context = {'allPost': allPosts}
	return render(request , "home/about.html" , context)


def privacy(request):
	# messages.success(request , "Welcome To The Privacy Policy ")
	allPosts = Privacy.objects.all().first()
	context = {'allPost': allPosts}
	return render(request , "home/privacy.html" , context)




def login(request):
	return render(request, 'home/login.html')

# Sigup
def user_signup(request):
 if request.method == "POST":
  form = SignUpForm(request.POST)
  if form.is_valid():
   messages.success(request, 'Congratulations!! You have become an Author.')
   user = form.save()
   group = Group.objects.get(name='Author')
   user.groups.add(group)
 else:
  form = SignUpForm()
 return render(request, 'blog/signup.html', {'form':form})

# Login
def user_login(request):
 if not request.user.is_authenticated:
  if request.method == "POST":
   form = LoginForm(request=request, data=request.POST)
   if form.is_valid():
    uname = form.cleaned_data['username']
    upass = form.cleaned_data['password']
    user = authenticate(username=uname, password=upass)
    if user is not None:
     login(request, user)
     messages.success(request, 'Logged in Successfully !!')
     return HttpResponseRedirect('/dashboard/')
  else:
   form = LoginForm()
  return render(request, 'blog/login.html', {'form':form})
 else:
  return HttpResponseRedirect('/dashboard/')
