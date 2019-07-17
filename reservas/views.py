from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from main_app.models import *


class OfferList(ListView):

    template_name = "reservas/offers_listing.html"
    queryset = EmpleoOferta.objects.all()
    model = EmpleoOferta

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Ofertas"
        context['offers'] = self.queryset
        context['carreras'] = Carrera.objects.all()
        context['empleos'] = Empleo.objects.all()
        return context


class Offer(DetailView):

    template_name = "reservas/offer.html"
    context_object_name = 'offer'
    queryset = EmpleoOferta.objects.all()

    def get_object(self, queryset=None):
        id_ = self.kwargs.get("id")
        offer = get_object_or_404(EmpleoOferta, id=id_)
        return offer

