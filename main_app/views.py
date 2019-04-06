from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render_to_response
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

class Login(TemplateView):

    template_name = 'main_app/login.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['title'] = 'Login'
        return context

def handler404(request, exception, template_name="404_error.html"):
    response = render_to_response("main_app/404_error.html")
    response.status_code = 404
    return response
