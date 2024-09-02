from django.urls import path
from . import views


urlpatterns = [
	path("", views.start, name = "start"),
	path("new/", views.new, name = "new"),
	path("new/<int:pk>", views.NewsDetailView.as_view(), name = 'news-detail'),
	path("podz/", views.podderzhka, name = "podz")
] 