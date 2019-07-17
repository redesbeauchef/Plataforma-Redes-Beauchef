from django.urls import path
from requerimientos.views import Requerimientos

urlpatterns = [
    path('', Requerimientos.as_view(), name='requerimientos'),
]