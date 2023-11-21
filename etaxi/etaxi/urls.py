from django.urls import path
from . import views

app_name = 'etaxi'
urlpatterns = [
    path('', views.home, name='home'),
    path('contacts/', views.contacts, name='contacts'),
    path('about/', views.about, name='about'),
    
] 