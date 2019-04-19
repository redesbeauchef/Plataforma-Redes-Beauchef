from .views import RedirectLoginView, RegisterForm, PerfilCreate
from django.contrib.auth import views as viewsauth
from django.urls import path

urlpatterns = [
    path('login/', viewsauth.LoginView.as_view(), name='login'),
    path('registrar/', RegisterForm.as_view(), name='register'),
    path('perfilcreate/', PerfilCreate.as_view(), name='perfilcreate'),
    path('perfil/', RedirectLoginView.as_view(), name='profile')

]