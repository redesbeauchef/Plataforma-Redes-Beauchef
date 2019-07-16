from django.shortcuts import render
from django.views.generic import TemplateView


class OfferList(TemplateView):

    template_name = "reservas/offers_listing.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Ofertas"
        return context