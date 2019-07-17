from .views import OfferList, Offer
from django.urls import path

urlpatterns = [
    path('ofertas/', OfferList.as_view(), name='ofertas'),
    path('oferta', Offer.as_view(), name='oferta')
]
