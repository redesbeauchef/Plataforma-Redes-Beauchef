from .views import RedirectLoginView, PerfilCreate
from django.contrib.auth import views as viewsauth
from django.urls import path

urlpatterns = [
    path('login/', viewsauth.LoginView.as_view(), name='login'),
    path('registrar/', PerfilCreate.as_view(), name='register'),
    path('perfil/', RedirectLoginView.as_view(), name='profile')

]