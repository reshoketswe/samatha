from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms

class UserRegistration(UserCreationForm):
	email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

	class meta:
		model = User
		fields = ('username', 'email', 'password1', 'password2' )