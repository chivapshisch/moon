from django.shortcuts import render 
from register.forms import PeopleForm
from register.models import People
from vhod.forms import NewForm
from hosty.models import New

def vhod(request):
	error = ''
	log = ''
	if request.method == 'POST':
		form = PeopleForm(request.POST)
		if form.is_valid():
			log = request.POST['login']
			pas = request.POST['password']	
			q = People.objects.filter(login=log, password=pas)
			for i in q:
				if i.login == log and i.password == pas:
					print(log)
					return render(request, "vhod/html/account.html", {'log': log})
		else:
			error = 'ошибка'
	form = PeopleForm()
	print(log)
	data = {
		'form': form,
		'error': error,
		'log': log,
	}

	return render(request, "register/html/register.html", data)
 

def makenews(request):
	error = ''

	if request.method == 'POST':
		form = NewForm(request.POST)
		if form.is_valid():
			form.save()
			return render(request, "vhod/html/account.html")
		else: 
			error = 'Неправильно заполнена форма'
	form = NewForm()
	data = {
		'error': error,
		'form': form
	}

	return render(request, "vhod/html/makenews.html", data)