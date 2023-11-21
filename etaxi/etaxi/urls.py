from django.urls import path
from . import views

app_name = 'etaxi'
urlpatterns = [
    path('', views.home, name='home'),
    path('etaxi/<str:city>', views.home, name='homecity'),
    path('etaxi/<str:city>/contacts/', views.contacts, name='contacts'),
    path('etaxi/<str:city>/about/', views.about, name='about'),    
] 