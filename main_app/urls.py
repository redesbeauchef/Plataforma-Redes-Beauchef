from django.urls import path

from main_app.views import IndexView, AboutView, Login, FaqView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('sobre-nosotros', AboutView.as_view(), name='about'),
    path('preguntas-frecuentes', FaqView.as_view(), name='faq'),
    path('login', Login.as_view(), name='login')
]