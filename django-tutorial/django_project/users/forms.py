from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile


class UserRegisterForm(UserCreationForm):
	email = forms.EmailField(required=True)

	#Classe meta cria uma configuração e a mantém em um único local
	class Meta:
		#Especifica o model que esse form interagirá
		model = User
		#Campos que serão mostrados no formulário
		fields = ['username', 'email', 'password1', 'password2']

class UserUpdateForm(forms.ModelForm):
	email = forms.EmailField()

	class Meta:
		model = User
		fields = ['username', 'email']

class ProfileUpdateForm(forms.ModelForm):
	class Meta:
		model = Profile
		fields = ['image']

