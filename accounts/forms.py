from django import forms
from main_app.models import Perfil, User


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'password']

class PerfilForm(forms.ModelForm):
    class Meta:
        model = Perfil
        exclude = ['usuario']
