from django.urls import path, include

from main_app.views import IndexView, AboutView, Login

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('sobre-nosotros', AboutView.as_view(), name='about'),
    path('requerimientos', include('requerimientos.urls'))
]