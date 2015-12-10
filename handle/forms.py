from django import forms
from .models import Registration

class RegistrationForm(forms.ModelForm):
	class Meta:
		model = Registration
		widgets = {
		'password':forms.PasswordInput(),
		}
		fields='__all__'
