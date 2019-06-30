from django.shortcuts import render
from django.views.generic import TemplateView
from main_app.models import Carrera

# Create your views here.
class Requerimientos(TemplateView):

    template_name = 'requerimientos/requirements.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['title'] = 'requerimientos'
        context['carreras'] = Carrera.objects.all().order_by('plan')
        return context