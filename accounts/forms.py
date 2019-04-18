from django import forms
from main_app.models import Perfil


class PerfilCreateForm(forms.ModelForm):
    class Meta:
        model = Perfil
        fields = ['usuario', 'egresados', 'rut', 'email', 'carrera', 'empleo', 'cv', 'foto_perfil', 'perfil_pro', 'ano_ingreso', 'ano_egreso', 'spam', 'eula']
