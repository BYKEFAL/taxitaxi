from django.shortcuts import render, redirect, HttpResponse, HttpResponseRedirect
from django.template.response import TemplateResponse
import requests
import json
from ipware import get_client_ip
from django.contrib.gis.geoip2 import GeoIP2
from dadata import Dadata
from .models import *
from .forms import DriverAddForm, DriverAddFormOffer, DriverAddFormQuest

# Определение города на Русском по IP
token = "d1b7f800e7beb52dbc7b32f8f140808fe8e7bfaa"
dadata = Dadata(token)

# def geo(request):
#     client_ip, is_routable = get_client_ip(request)
#     client_ip = '176.59.144.81' #Тестовый IP не забыть удалить
#     response = dadata.iplocate(client_ip)['data']['city']
#     return response
    
    
def home(request, city='Иркутск'):
    
    # geos = geo(request)
    # print(geos)
    
    cities = CityPark.objects.all()
    citygeo = CityPark.objects.get(name=city)
    
    novalid = None
    if request.method == "POST":
        form = DriverAddForm(request.POST)
        formoffer = DriverAddFormOffer(request.POST)
        if form.is_valid():
            form.save()
            form = DriverAddForm()
            return redirect('/')
        elif formoffer.is_valid():
            formoffer.save()
            formoffer = DriverAddFormOffer()
            return redirect('/')
        else:
            novalid = True
            
    else:
        form = DriverAddForm()
        formoffer = DriverAddFormOffer()
        
    context = {'cities': cities, 'form': form, 
               'formoffer': formoffer, 'novalid': novalid, 'citygeo': citygeo}
   
    return render(request, 'index.html', context)



def about(request, city):
    cities = CityPark.objects.all()
    citygeo = CityPark.objects.get(name=city)
    
    novalid = None
    if request.method == "POST":
        form = DriverAddForm(request.POST)
        formquest = DriverAddFormQuest(request.POST)
        if formquest.is_valid():
            formquest.save()
            formquest = DriverAddFormQuest()
            return redirect(request.META.get('HTTP_REFERER'))
        elif form.is_valid():
            form.save()
            form = DriverAddForm()
            return redirect(request.META.get('HTTP_REFERER')) 
        else:
            novalid = True
    else:
        form = DriverAddForm()
        formquest = DriverAddFormQuest()
    context = {'form': form, 'novalid': novalid, 'formquest': formquest, 'cities': cities, 'citygeo': citygeo}
    return render(request, 'etaxi/pageAboutUs.html', context)

def contacts(request, city):
    cities = CityPark.objects.all()
    citygeo = CityPark.objects.get(name=city)
    
    novalid = None
    if request.method == "POST":
        form = DriverAddForm(request.POST)
        if form.is_valid():
            form.save()
            form = DriverAddForm()
            return redirect(request.META.get('HTTP_REFERER'))
            # return redirect('/contacts')
        else:
            novalid = True
    else:
        form = DriverAddForm()
        
    context = {'form': form, 'novalid': novalid, 'cities': cities, 'citygeo': citygeo}
    return render(request, 'etaxi/pageContacts.html', context)    
    
    
'''
Получение ip клиента через х-форвардед-фор, с последующим получением данных о Геолокации чере стороннее API Abstract

api_key = '50382ebb31d94b6ab016be31d1f17420'
api_url = f'https://ipgeolocation.abstractapi.com/v1/?api_key={api_key}'

def get_ip_geolocation_data(ip_address):
   response = requests.get(api_url + "&ip_address=" + ip_address)
   print(response.content)  
   return response.content

def home(request):
   x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
   if x_forwarded_for:
       ip = x_forwarded_for.split(',')[-1].strip()
   else:
       ip = request.META.get('REMOTE_ADDR')
   geolocation_json = get_ip_geolocation_data(ip)
   geolocation_data = json.loads(geolocation_json)
   country = geolocation_data['country']
   region = geolocation_data['region']
   city = geolocation_data['city']
   return HttpResponse(f'WELCOME {ip} страна {country} region {region} city {city}')
   
'''


# Определение города через Geoip2
# def home(request):
# #    client_ip, is_routable = get_client_ip(request)
# #    client_ip = '176.59.144.81' #Новосибирск
#    client_ip = '84.17.51.52'
#    if client_ip is not None:
#     g = GeoIP2()
#     try:
#         location = g.city(client_ip)['city']
#     except:
#         location = {'Локация': 'нет данных'}
   
#    print(client_ip)
#    return HttpResponse(f'WELCOME {client_ip} {location}')

#создание карты на сайте






   


