from django.shortcuts import render
from .forms import PeopleForm
from .models import People
 
def register(request):
	error = ''
	if request.method == 'POST':
		form = PeopleForm(request.POST)
		if form.is_valid():
			form.save()
			return render(request, "register/html/nice.html")
		else:
			error = 'ошибка'
	form = PeopleForm()

	data = {
		'form': form,
		'error': error
	}

	return render(request, "register/html/register.html", data)
 