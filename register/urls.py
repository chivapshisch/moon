from django.urls import path
from . import views


urlpatterns = [
	path("now/", views.register, name = "reg"),
] 