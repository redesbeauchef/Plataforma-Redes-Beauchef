from django import forms
from main_app.models import Perfil, User


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['password', 'email', 'first_name', 'last_name']

class PerfilForm(forms.ModelForm):
    class Meta:
        model = Perfil
        #exclude = ['usuario']
        fields = ['usuario', 'egresado', 'rut', 'carrera', 'empleo', 'cv', 'foto_perfil', 'perfil_pro', 'ano_ingreso', 'ano_egreso', 'spam', 'eula']
