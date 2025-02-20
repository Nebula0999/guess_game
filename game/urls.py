from django.urls import path
from . import views

urlpatterns = [
    path('', views.guess_gender, name='index'),
]