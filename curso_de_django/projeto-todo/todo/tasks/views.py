from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .models import Task
from .forms import TaskForm
from django.contrib import messages
from django.core.paginator import Paginator

def helloWorld(request):
	return HttpResponse("Hello world")

@login_required
def taskList(request):

	#Trata da seleção de busca
	search = request.GET.get('search')

	#Trata do filtro de status
	filter = request.GET.get('filter')

	if search:
		tasks = Task.objects.filter(title__icontains=search, user=request.user)

	elif filter:
		#Filtra através do filtro de pesquisa
		tasks = Task.objects.filter(done=filter, user=request.user)		

	else:
		tasks_list = Task.objects.all().order_by('-created_at').filter(user=request.user)

		#Passa a lista de tasks e a quantidade de tasks por página
		paginator = Paginator(tasks_list, 3)

		#Recebe do request o argumento page, que virá junto à URL. É o identificador de que página o user está
		page = request.GET.get('page')

		#Pega a página atual, conseguindo exibir o número corretos de tasks por página
		tasks = paginator.get_page(page)

	return render(request, 'tasks/list.html', {'tasks':tasks})

def yourName(request, name):
	return render(request, 'tasks/yourname.html', {'name':name})

@login_required
def taskView(request, id):
	task = get_object_or_404(Task, pk=id)
	return render(request, 'tasks/task.html', {'task':task})

@login_required
def newTask(request):

	#Verifica se existe um envio do tipo POST 
	if request.method == 'POST':
		form = TaskForm(request.POST)

		if form.is_valid():

			#Pausa o salvamento da tarefa para setar o valor de done. Depois, salva a tarefa
			task = form.save(commit=False)
			task.done = 'doing'
			task.user = request.user
			task.save()
			return redirect('/')

	else:	
		form = TaskForm()
		return render(request, 'tasks/addtask.html', {'form':form})

@login_required
def editTask(request, id):
	print("hi")

	#Retorna o objeto ou 404
	task = get_object_or_404(Task, user=request.user, pk=id)
	#Deixa o formulário pré populado para edição
	form = TaskForm(instance=task)

	#Verifica se o formulário está sendo enviado ou requisitado
	if(request.method == 'POST'): #É disparado quando o formulário de edição for enviado
		form = TaskForm(request.POST, instance=task)
		if(form.is_valid()):
			task.save()
			return redirect('/')
		else:
			#Se houver erro retorna a própria tarefa
			return render(request, 'tasks/edittask.html', {'form':form, 'task':task})

	else:
		return render(request, 'tasks/edittask.html', {'form':form, 'task':task})

@login_required
def deleteTask(request, id):
	print("OI")
	task = get_object_or_404(Task, user=request.user, pk=id)
	task.delete()

	#Retorna uma mensagem para o usuário
	messages.info(request, 'Tarefa deletada com sucesso')



	return redirect('/')

@login_required
def changeStatus(request, id):
	task = get_object_or_404(Task, user=request.user, pk=id)

	if task.done == 'doing':
		task.done = 'done'
	else:
		task.done = 'doing'

	task.save()

	return redirect('/')


