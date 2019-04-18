from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse_lazy
from main_app.models import Perfil
from django.views.generic import TemplateView, CreateView
from accounts.forms import PerfilCreateForm


class RedirectLoginView(TemplateView):

    template_name = "candidate_profile.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Index"
        return context

class PerfilCreate(CreateView):
    template_name = 'register.html'
    form_class = PerfilCreateForm
    # def get(self, request, *args, **kwargs):
    #     context = {'form': PerfilCreateForm()}
    #     return render(request, 'register.html', context)
    #
    # def post(self, request, *args, **kwargs):
    #     form = PerfilCreateForm(request.POST)
    #     if form.is_valid():
    #         book = form.save()
    #         book.save()
    #         return HttpResponseRedirect(reverse_lazy('perfil:profile', args=[book.id]))
    #     return render(request, 'register.html', {'form': form})

