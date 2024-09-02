from django.db import models


class New(models.Model):
	title = models.CharField(max_length = 40)
	main_text = models.CharField(max_length = 3000)
	author = models.CharField(max_length = 25)

	def __str__(self):
		return (self.title)

