from .models import People
from django.forms import ModelForm, TextInput

class PeopleForm(ModelForm):
	class Meta:
		model = People
		fields = ['login', 'password']

		widgets = {
			'login': TextInput(attrs={
				'class': 'login',
				'placeholder': 'Имя',
				}),

			'password': TextInput(attrs={
				'class': 'password',
				'placeholder': 'Пароль'
				})
		} 