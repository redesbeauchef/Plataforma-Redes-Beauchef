from django.urls import path

from main_app.views import IndexView, AboutView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('sobre-nosotros', AboutView.as_view(), name='about'),
]