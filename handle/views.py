from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from django.contrib.auth.hashers import make_password
from forms import RegistrationForm
from .models import Registration
import re,random

# If the user already logged in, redirect him to his page
def index(request):
	context = {}
	if request.session.get('handle'or None):
		handle = request.session['handle']
		context['feeds'] = 3*handle
		form = Registration.objects.get(handle=handle)
		return render(request,'handle/codegress.html',context)
	else:
		context['signup'] = True
		context['login'] = True
		return render(request,'handle/index.html',context)

# search for user leaderboard information
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
	context['login'] = True
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
							form = Registration(first_name=fname,last_name=lname,country=country,email=email,handle=handle,password=paswrd)
							form.save()
							return render(request,"handle/login.html",context)
						else: 
							context['error'] = 'Secure passwords should have atleast\na number and a special character'
					elif not email_flag:
						context['error'] = 'Email already registered.'
						request.session['email'] = email
						context['forgot'] = True
					elif not handle_flag:
						context['error'] = 'Username not available.'
				else:
					context['error'] = 'Username should contain only alphabets'
			except ValidationError:
				context['error'] = "Email is invalid"
		else:
			context['error'] = "Fields can't be empty."
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
	context['signup'] = True
	if request.session.get('handle'or None):
		return HttpResponseRedirect('/')
	elif request.method == 'POST':
		current_handle = request.POST.get('handle',None)
		current_password = request.POST.get('password',None)
		if current_handle and current_password:
			context['handle'] = current_handle
			try:
				if '@' in current_handle:
					validate_email(current_handle)
					form = Registration.objects.get(email=current_handle)
					request.session['email'] = current_handle
					current_handle = form.handle
				else:	
					form = Registration.objects.get(handle=current_handle)
				
				if form.password == current_password:
					request.session['handle'] = current_handle
					return HttpResponseRedirect('/')
				else:
					context['error'] = "Email / Password isn't correct"
					context['focus'] = False
			except ValidationError:
				context['error'] = "Email is Invalid."
			except Registration.DoesNotExist:
				context['focus'] = True
				context['error'] = "Username / Email not registered."
		else:
			context['error'] = "Fields can't be empty."
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
				if request.session.get('email' or None):
					del request.session['email']
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
	if request.session.get('email' or None):
		del request.session['email']
	return HttpResponseRedirect('/')

# Redirects to User's page on success or to 404 page
def leaderboard(request,handle):
	context = {}
	context['login'] = True
	context['signup'] = True
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
			if rank%10 == 1:
				context['suffix'] = 'st'
			elif rank%10 == 2:
				context['suffix'] = 'nd'
			elif rank%10 == 3:
				context['suffix'] = 'rd'
			else:
				context['suffix'] = 'th'
			context['rank'] = rank
		else:
			context['rank'] = 1
			context['suffix'] = 'st'
		return render(request,'handle/leaderboard.html',context)
	except Registration.DoesNotExist:
		context['error'] = "PAGE NOT FOUND"
		context['error_desc'] = "404 error"
		return render(request,'handle/404.html',context)

def challenges(request):
	context = {'error':'Nothing new to display yet..'}
	return render(request,'handle/codegress.html',context)

def competitions(request):
	context = {'error':'Nothing new to display yet..'}
	return render(request,'handle/codegress.html',context)

def updates(request):
	context = {'error':'Nothing new to display yet..'}
	return render(request,'handle/codegress.html',context)

def messages(request):
	context = {'error':'Nothing new to display yet..'}
	return render(request,'handle/codegress.html',context)

def recent(request):
	context = {'error':'Nothing new to display yet..'}
	return render(request,'handle/codegress.html',context)

def profile(request,selected):
	context = {}
	fields = {'personal':True,'password':True,'group':True,'challenges':True,'feeds':True}
	if request.session.get('handle' or None):
			handle = request.session['handle']
			form = Registration.objects.get(handle=handle)
			context['fn'] = form.first_name
			context['ln'] = form.last_name
			context['email'] = form.email
			context['country'] = form.country
			try: 
				if fields[selected]:
					context['selected_list_item'] = selected
					html_url = "handle/profile_"+selected+".html"
					return render(request,html_url,context)
			except KeyError:
				pass
	return HttpResponseRedirect("/settings/personal",context)

def follow(request,handle):
	return HttpResponse(request.session['handle']+' => '+handle)
