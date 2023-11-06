from django.urls import path
from . import views

app_name = 'etaxi'
urlpatterns = [
    path('', views.home, name='home'),
    
] 