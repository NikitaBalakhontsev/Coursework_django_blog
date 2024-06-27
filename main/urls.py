from django.contrib.auth import login
from django.urls import path

from main import views

urlpatterns = [
    path('', views.index, name='home'),
    path('about/', views.about, name='about'),

]