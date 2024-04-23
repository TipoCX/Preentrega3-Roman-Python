from django import forms
from .models import *

class UserCreateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['name', 'password', 'group_user']
        labels = {
            'name': 'Elegir un nombre para el usuario',
            'password': 'Ingresar contraseña',
            'group_user': 'Seleccione el grupo al que pertenese'
        }


class GroupCreateForm(forms.ModelForm):
    class Meta:
        model = Group
        fields = ['alias', 'description', 'creator']
        labels = {
            'Alias': 'Elegir un nombre para el grupo',
            'Description': 'descripcion del grupo',
            'Creator': 'Seleccione al creador del grupo'
        }

class SendMessageForm(forms.Form):
    content = forms.CharField(label="Send Message")
