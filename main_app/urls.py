from django.urls import path

from main_app.views import IndexView

urlpatterns = [
    path('', IndexView.as_view()),
]