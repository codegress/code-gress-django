from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from django.contrib.auth.hashers import make_password
from forms import RegistrationForm
from .models import Registration,Problem,Solution,SampleCase
import re,random,json

valid_signups = {}
testcases = []
# If the user already logged in, redirect him to his page
def index(request):
	context = {}
	if request.session.get('handle'or None):
		handle = request.session['handle']
		context['feeds'] = 3*handle
		context['handle'] = handle;
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
		handle = request.POST.get('handle' or None)
		email = request.POST.get('email' or None)
		paswrd = request.POST.get('password' or None)

		# Making sure fields are not empty
		if email and handle and paswrd:
			try:
				validate_email(email)
				context['email'] = email
				if re.match('[a-zA-Z]+',handle):
					handle_flag = validate(handle)
					email_flag = validate(email)
					context['handle'] = handle
					if handle_flag and email_flag:
						if validate_password(paswrd):
							form = Registration(email=email,handle=handle,password=paswrd)
							form.save()
							return render(request,"handle/login.html",context)
						else: 
							context['error'] = 'Secure passwords should include numbers &  special characters'
					
					elif not handle_flag:
						context['error'] = 'Username not available.'

					elif not email_flag:
						context['error'] = 'Email already registered.'
						request.session['email'] = email
						context['forgot'] = True
				else:
					context['error'] = 'Username should contain only alphabets'
			except ValidationError:
				context['error'] = "Email is invalid"
		else:
			context['error'] = "Fields can't be empty."
	return render(request,'handle/signup.html',context)

def check_handle(request):
	response = {}
	global valid_signups
	if request.method == 'POST':
		handle = request.POST.get('handle' or None)
		if re.match('^[a-zA-Z]{3,}$',handle):
			response['valid'] = True
			response['valid_feedback'] = None;
			try:
				Registration.objects.get(handle=handle)
				response['registered'] = True
				response['reg_feedback'] = "'"+handle+"' is already taken."
			except Registration.DoesNotExist:
				response['registered'] = False
		else:
			response['valid'] = False
			response['valid_feedback'] = "Minimum of length 3";
	valid_signups['handle'] = response['valid'] and not response['registered']
	json_data = json.dumps(valid_signups)
	return HttpResponse(json_data,content_type="application/json")

def check_email(request):
	global valid_signups
	if request.method == 'POST':
		email = request.POST.get('email' or None)
		try:
			Registration.objects.get(email=email)
			valid_signups['email'] = False
			valid_signups['info'] = 'Email already Registered'
		except Registration.DoesNotExist:
			valid_signups['email'] = True
			valid_signups['info'] = None
	json_data = json.dumps(valid_signups)
	return HttpResponse(json_data,content_type="application/json")

# check for whether username and/or email exists already
def validate(handle):
	registered = False
	try:
		if '@' in handle:
			form = Registration.objects.get(email=handle)
		else:
			form = Registration.objects.get(handle=handle)
		registered = True
	except Registration.DoesNotExist:
		registered = False
	return not registered

# Password validation ([0-9], [a-zA-Z] and special chars)
def validate_password(password):
	return re.match('([a-zA-Z0-9]{1,})',password) != None

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
		if handle != request.session.get('handle'):
			context['follow'] = True
		context['handle'] = handle
		context['country'] = form.country
		context['company'] = form.company
		context['website'] = form.website
		context['email'] = form.email
		context['fname'] = form.full_name
		rank = int(random.random()*random.random()*100)
		if rank != 0:
			context['rank'] = rank
			if rank >= 11 and rank <= 13:
				context['suffix'] = 'th'
			elif rank%10 == 1:
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

def challenges(request,id):
	context = {}
	if request.session.get('handle' or None):
		if id:
			try:
				problem = Problem.objects.get(id=id)
				context['problem'] = problem
				return render(request,'handle/challenge.html',context)
			except Problem.DoesNotExist:
				pass
		handle = request.session.get('handle')
		handle = Registration.objects.get(handle=handle)
		problems = Problem.objects.filter(handle=handle)
		context['challenges'] = True
		context['problems'] = problems
	else:
		HttpResponseRedirect('/signin')
	return render(request,'handle/challenge.html',context)

def new_challenge(request):
	return render(request,'handle/new_challenge.html')

def testcase(request):
	if request.is_ajax():
		sample_in = request.GET.get('input')
		sample_out = request.GET.get('output')
		testcases += [{'input':sample_in,'output':sample_out}]
	json_data = json.dumps(testcases)
	return HttpResponse(json_data,content_type="application/json")

def competitions(request):
	context = {'error':'Nothing new to display yet..'}
	return render(request,'handle/codegress.html',context)

def updates(request):
	context = {'error':'Nothing new to display yet..'}
	return render(request,'handle/codegress.html',context)

def messages(request):
	context = {'error':'Nothing new to display yet..'}
	return render(request,'handle/codegress.html',context)

def profile(request,selected):
	context = {}
	fields = {'personal':True,'password':True,'group':True,'challenges':True,'feeds':True}
	if request.session.get('handle' or None):
			handle = request.session['handle']
			form = Registration.objects.get(handle=handle)
			context['fname'] = form.full_name
			context['email'] = form.email
			
			if form.country:
				context['country'] = form.country
			
			if form.company:
				context['company'] = form.company
			
			if form.website:
				context['website'] = form.website
			
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
