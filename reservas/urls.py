from .views import OfferList
from django.urls import path

urlpatterns = [
    path('ofertas/', OfferList.as_view(), name='ofertas')
]
