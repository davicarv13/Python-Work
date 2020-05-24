from django.shortcuts import render

#Formulário para criação de conta
from django.contrib.auth.forms import UserCreationForm

#Igual o redirect, mas para classes bases views esse deve ser usado
from django.urls import reverse_lazy

#Quem permite a criação de classes based views
from django.views import generic

class SignUp(generic.CreateView):

	#Definição do formulário
	form_class = UserCreationForm

	#Define a URL de redirecinamento caso o registro seja bem sucedido
	success_url = reverse_lazy('login')

	#Define o local do template de registro, no caso, na pasta ../templates/registration/
	template_name = 'registration/register.html'


