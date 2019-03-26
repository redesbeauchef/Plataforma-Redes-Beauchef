from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView

class IndexView(TemplateView):

    template_name = "main_app/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Index"
        return context

class AboutView(TemplateView):

    template_name = "main_app/about.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Sobre nosotros"
        return context
