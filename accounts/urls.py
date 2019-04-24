from accounts.forms import UserAuthenticationForm
from .views import RedirectLoginView, RegisterForm
from django.contrib.auth import views as viewsauth
from django.urls import path

urlpatterns = [
    path('login/',
         viewsauth.LoginView.as_view(template_name='registration/login.html', form_class=UserAuthenticationForm),
         name='login'),
    path('registrar/', RegisterForm.as_view(), name='register'),
    path('perfil/', RedirectLoginView.as_view(), name='profile'),
    path('logout/', viewsauth.LogoutView.as_view(), name='logout')

]
