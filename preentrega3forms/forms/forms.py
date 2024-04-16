from django import forms
from .models import *

class UserCreateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['name', 'password']
        labels = {
            'name': 'Elegir un nombre para el usuario',
            'password': 'Ingresar contraseña',
        }
