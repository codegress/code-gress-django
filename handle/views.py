from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from forms import RegistrationForm
from .models import Registration
import re,random
from django.contrib.auth.hashers import make_password
# Create your views here.

# If the user logged already, redirects him to his page or else to the home page
def index(request):
	context = {}
	if request.session.get('handle'or None):
		handle = request.session['handle']
		context['feeds'] = handle
		form = Registration.objects.get(handle=handle)
		return render(request,'handle/codegress.html',context)
	else:
		context['signup'] = True
		context['login'] = True
		return render(request,'handle/index.html',context)

def search(request):
	context = {}
	if request.GET['q']:
		handle = request.GET['q']
		return leaderboard(request,handle)
	else:
		context['info'] = "404 page not found"
	return render(request,'handle/404.html',context)
# signup redirects to login if success
def signup(request):
	context = {}
	if request.session.get('handle'or None):
		return HttpResponseRedirect('/')
	elif request.method == 'POST':
		fname = request.POST.get('first_name' or None)
		lname = request.POST.get('last_name' or None)
		country = request.POST.get('country' or None)
		email = request.POST.get('email' or None)
		handle = request.POST.get('handle' or None)
		paswrd = request.POST.get('password' or None)

		# Making sure fields are not empty
		if fname and lname and country and email and handle and paswrd:
			context['fname'] = fname
			context['lname'] = lname
			context['country'] = country
			try:
				validate_email(email)
				context['email'] = email
				if re.match('[a-zA-Z]+',handle):
					handle_flag = validate_handle(handle)
					email_flag = validate_handle(email)
					if handle_flag and email_flag:
						context['handle'] = handle
						if validate_password(paswrd):
							# paswrd = make_password(password=paswrd,salt=None,hasher='default')
							form = Registration(first_name=fname,last_name=lname,country=country,email=email,handle=handle,password=paswrd)
							form.save()
							return render(request,"handle/login.html",context)
						else: 
							context['error'] = 'Secure passwords should have atleast\na number and a special character'
					elif not email_flag:
						context['error'] = 'Email already registered.'
						context['forgot'] = True
					elif not handle_flag:
						context['error'] = 'Username not available.'
				else:
					context['error'] = 'Username should contain only alphabets'
			except ValidationError:
				context['error'] = "Email is invalid"
		else:
			context['error'] = "Fields can't be empty."
	else:
		context['login'] = True
	return render(request,'handle/signup.html',context)

# check for whether username and/or email exists already
def validate_handle(handle):
	registered = False
	try:
		if '@' in handle:
			form = Registration.objects.get(email=handle)
		else:
			form = Registration.objects.get(handle=handle)
		registered = True
	except Registration.DoesNotExist:
		registered = False
	return  not registered

# Password validation ([0-9], [a-zA-Z] and special chars)
def validate_password(password):
	num = re.search('[0-9]+',password)
	char = re.search('[a-zA-Z]+',password)
	special = re.search('[\!\@\#\$\^\&\*\(\)\~]{1}',password)
	return num and char and special

# Login verfication and session management
def login(request):
	context = {}
	if request.session.get('handle'or None):
		return HttpResponseRedirect('/')
	elif request.method == 'POST':
		current_handle = request.POST.get('handle',None)
		current_password = request.POST.get('password',None)
		if current_handle and current_password:
			try:
				if '@' in current_handle:
					validate_email(current_handle)
					form = Registration.objects.get(email=current_handle)
					current_handle = form.handle
				else:	
					form = Registration.objects.get(handle=current_handle)
				
				if form.password == current_password:
					request.session['handle'] = current_handle
					request.session['fname'] = form.first_name
					request.session['lname'] = form.last_name
					return HttpResponseRedirect('/')
				else:
					context['handle'] = current_handle
					context['error'] = "Password isn't matched."
					context['focus'] = False
			except ValidationError:
				context['error'] = "Email is Invalid."
			except Registration.DoesNotExist:
				context['focus'] = True
				context['error'] = "Username / Email not registered."
		else:
			context['error'] = "Fields can't be empty."
	else:
		context['signup'] = True
	return render(request,'handle/login.html',context)

# password recovery returns to same page (with messages and/or errors)
def recover(request):
	context = {}
	if request.method == 'POST':
		recover_email = request.POST.get('email' or None)
		if recover_email:
			try:
				validate_email(recover_email)
				form = Registration.objects.get(email=recover_email)
				context['info'] = "Email Sent."
			except ValidationError:
				context['error'] = 'Email is invalid'
			except Registration.DoesNotExist:
				context['error'] = "Email isn't registered yet."
			except:
				context['error'] = "Something is wrong"
		else:
			context['error'] = "Email can't be empty"
	return render(request,'handle/recover.html',context)

# deletes current user handle's session and returns to home page
def logout(request):
	if request.session.get('handle'or None):
		del request.session['handle']
	return HttpResponseRedirect('/')

# Redirects to User's page on success or to 404 page
def leaderboard(request,handle):
	context = {}
	try:
		form = Registration.objects.get(handle=handle)
		context['handle'] = handle
		context['country'] = form.country
		context['email'] = form.email
		context['fname'] = form.first_name
		context['lname'] = form.last_name
		rank = int(random.random()*random.random()*100)
		if rank != 0:
			context['rank'] = rank
		else:
			context['rank'] = 1
		return render(request,'handle/leaderboard.html',context)
	except Registration.DoesNotExist:
		context['error'] = "PAGE NOT FOUND"
		context['error_desc'] = "404 error"
		return render(request,'handle/404.html',context)

def challenges(request):
	return render(request,'handle/codegress.html')

def competitions(request):
	return render(request,'handle/codegress.html')

def updates(request):
	return render(request,'handle/codegress.html')

def messages(request):
	return render(request,'handle/codegress.html')

def recent(request):
	return render(request,'handle/codegress.html')

def profile(request,selected):
	context = {}
	items = ['personal','password','group','challenges','feeds']
	if request.session.get('handle' or None):
			handle = request.session['handle']
			form = Registration.objects.get(handle=handle)
			context['fn'] = form.first_name
			context['ln'] = form.last_name
			context['email'] = form.email
			context['country'] = form.country
			if selected in items:
				context['selected_list_item'] = selected
				html_url = "handle/profile_"+selected+".html"
				return render(request,html_url,context)
	return HttpResponseRedirect("/settings/personal")
