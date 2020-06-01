from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.views.generic import (
	ListView, 
	DetailView, 
	CreateView,
	UpdateView,
	DeleteView, 
	)
from django.http import HttpResponse

from .models import Post

def home(request):
	context = {
		'posts':Post.objects.all()
	}
	return render(request, 'blog/home.html', context)

class PostListView(ListView):
	#Variavel de nome 'model' define qual o modelo da view
	model = Post
	#Substitui o nome padrão de templates para class based view do Django
	template_name = 'blog/home.html' #<app>/<model>_<viewtype>.html
	#Injeta os posts no template, na variavel 'posts'
	context_object_name = 'posts'
	#Ordena os posts pela data de criação
	ordering = ['-date_posted']
	#Limita o número de posts para 2 por página
	paginate_by = 5

class UserPostListView(ListView):
	#Variavel de nome 'model' define qual o modelo da view
	model = Post
	#Substitui o nome padrão de templates para class based view do Django
	template_name = 'blog/user_posts.html' #<app>/<model>_<viewtype>.html
	#Injeta os posts no template, na variavel 'posts'
	context_object_name = 'posts'
	#Limita o número de posts para 2 por página
	paginate_by = 5

	#Override
	def get_queryset(self):
		user = get_object_or_404(User, username=self.kwargs.get('username'))
		return Post.objects.filter(author=user).order_by('-date_posted')


class PostDetailView(DetailView):
	#Variavel de nome 'model' define qual o modelo da view
	model = Post

class PostCreateView(LoginRequiredMixin, CreateView):
	#Variavel de nome 'model' define qual o modelo da view
	model = Post
	fields = ['title', 'content']

	#Override do método de validação do form
	def form_valid(self, form):
		form.instance.author = self.request.user
		return super().form_valid(form)

#UpdateView deve ser o último parâmetro
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
	#Variavel de nome 'model' define qual o modelo da view
	model = Post
	fields = ['title', 'content']

	#Override do método de validação do form
	def form_valid(self, form):
		form.instance.author = self.request.user
		return super().form_valid(form)

	def test_func(self):
		#Pega o post que está sendo atualizado
		post = self.get_object()

		#Verifica se autor do post é igual ao usuário logado
		if self.request.user == post.author:
			return True
		else:
			return False

#DeleteView deve ser o último parâmetro
class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
	#Variavel de nome 'model' define qual o modelo da view
	model = Post
	#Redirecionamento quando o post for deletado
	success_url = '/'
	def test_func(self):
		#Pega o post que está sendo atualizado
		post = self.get_object()

		#Verifica se autor do post é igual ao usuário logado
		if self.request.user == post.author:
			return True
		else:
			return False

def about(request):
	return render(request, 'blog/about.html', {'title':'About'})




