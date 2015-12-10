from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from forms import RegistrationForm
from .models import Registration

# Create your views here.
def index(request):
	if request.session.get('handle'or None):
		return HttpResponseRedirect("/%s/"%request.session['handle'])
	else:
		return render(request,'handle/index.html')

def signup(request):
	context = {}
	if request.method == 'POST':
		form = RegistrationForm(request.POST or None)
		if form.is_valid():
			context['form'] = form
			form.save()
	else:
		context['form'] = RegistrationForm()
	return render(request,'handle/index.html',context)

def login(request):
	context = {}
	if request.session.get('handle'or None):
		return HttpResponseRedirect('/%s/' %request.session['handle'])
	elif request.method == 'POST':
		current_handle = request.POST.get('handle',None)
		current_password = request.POST.get('password',None)

		if current_handle and current_password:
			try:
				form = Registration.objects.get(handle=current_handle)
				if form.password == current_password:
					request.session['handle'] = current_handle
					return HttpResponseRedirect('/%s/' %current_handle)
				else:
					context['handle'] = current_handle
					context['error'] = "Password isn't matched."
					context['focus'] = False	
			except:
				context['focus'] = True
				context['error'] = "Username not registered."
		else:
			context['error'] = "Fields can't be empty."
	return render(request,'handle/login.html',context)

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
				context['error'] = 'Email is Invalid.'
			except Registration.DoesNotExist:
				context['error'] = "Email isn't registered yet."
			except:
				context['error'] = "Something is wrong."
		else:
			context['error'] = "Email can't be empty."
	return render(request,'handle/password_recover.html',context)

def logout(request):
	if request.session.get('handle'or None):
		del request.session['handle']
	return HttpResponseRedirect('/')

def leader(request,handle):
	# if request.session.get('handle' or None):
	# 	if request.session['handle'] == handle:
	# 		return render(request,'handle/codegress.html')
	# elif:
	try:
		form = Registration.objects.get(handle=handle)
	except Registration.DoesNotExist:
		return render(request,'handle/404.html')			
	return render(request,'handle/codegress.html')