from django.db import models

class People(models.Model):
	login = models.CharField(max_length = 8)
	password = models.CharField(max_length = 8)

	def __str__(self):
		return (self.login)