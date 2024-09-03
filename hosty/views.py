from django.shortcuts import render
from .models import New
from django.views.generic import DetailView

def start(request):
	return render(request, "hosty/html/glavn.html")

def new(request):
	data = New.objects.all()
	return render(request, "hosty/html/news.html", {'data': data})



class NewsDetailView(DetailView):
	model = New
	template_name = 'hosty/html/details_view.html'
	context_object_name = 'novost'


	print('fff')

def podderzhka(request): 
	return render(request, "hosty/html/podz.html")