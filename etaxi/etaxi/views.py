from django.shortcuts import render, redirect, HttpResponse, HttpResponseRedirect
from django.template.response import TemplateResponse
import requests
import json
from ipware import get_client_ip
from django.contrib.gis.geoip2 import GeoIP2
from geopy.distance import geodesic
from dadata import Dadata
from .models import *
from .forms import DriverAddForm, DriverAddFormOffer, DriverAddFormQuest

# Определение города на Русском по IP
token = "d1b7f800e7beb52dbc7b32f8f140808fe8e7bfaa"
dadata = Dadata(token)

#Определение города Dadata работает только по России
def geo(request):
    client_ip, is_routable = get_client_ip(request)
    # client_ip = '176.59.144.81' #Новосибирск
    # client_ip = '77.51.199.15' #Mocква, не забыть убрать тестовые IP
    try:
        response = dadata.iplocate(client_ip)['data']['city']
    except:
        response = 'нет данных'
    return response

# Определение города через Geoip2 по всему миру
def geo2(request):
    client_ip, is_routable = get_client_ip(request)
    # client_ip = '176.59.144.81' #Novosybirsk
    # client_ip = '77.51.199.15' #Moskow
    client_ip = '183.56.207.190' #Пекин, не забыть убрать тестовые IP
    try:
        g = GeoIP2()
        # location = g.city(client_ip)['city']
        location = g.city(client_ip)
    except:
        location = 'нет данных'
    return location

    
def home(request, city='nogeo'):
    
    cities = CityPark.objects.all()
    city_tuple_list = CityPark.objects.values_list('name')
    city_list = list(*zip(*city_tuple_list))
    
    #первый пуск сайта
    if city == 'nogeo':
        city = geo(request)
        #если город клиента определенный по IP совпал с одним из городов сайта
        if city in city_list:
            citygeo = CityPark.objects.get(name=city)
        else:
            try:
                #если не совпал, находим координаты, вычисляем расстояние до ближайшего города сайта и выводим инф. о нем.
                city_coords = geo2(request)
                unknown_city = (city_coords['latitude'], city_coords['longitude'])
                #получаем список кортежей с полями городов
                site_city_list = CityPark.objects.values_list('name', 'latitude', 'longitude')
                #создаем из списка c кортежами словарь город:координаты
                city_dict = {}
                for i in site_city_list:
                    city_dict[i[0]] = (i[1],i[2])
                #преобразуем в словарь город:минимальное расстояние
                distance_result_dict = {}
                for i in city_dict:
                    #вычисляем минимально расстояние и добавляем в словарь
                    result = geodesic(unknown_city, city_dict[i]).km
                    distance_result_dict[i] = result
                #заменяем наш стартовый город на город из словаря с минимальным расстоянием.
                city = min(distance_result_dict, key=distance_result_dict.get)    
                citygeo = CityPark.objects.get(name=city)
            except:
                city = 'Иркутск'
                citygeo = CityPark.objects.get(name=city)
    
    #когда клиент сменил город, запускать геолокация не будет
    else:
        citygeo = CityPark.objects.get(name=city)
        
    cars = TaxiCar.objects.filter(city=citygeo)
    novalid = None
    if request.method == "POST":
        form = DriverAddForm(request.POST)
        formoffer = DriverAddFormOffer(request.POST)
        driver_phone = request.POST['phone_number']
        if form.is_valid():
            form.save()
            driver = Driver.objects.get(phone_number=driver_phone)
            driver.city = citygeo
            driver.save()
            form = DriverAddForm()
            return redirect(request.META.get('HTTP_REFERER')) 
        elif formoffer.is_valid():
            formoffer.save()
            driver = Driver.objects.get(phone_number=driver_phone)
            driver.city = citygeo
            driver.save()
            formoffer = DriverAddFormOffer()
            return redirect(request.META.get('HTTP_REFERER')) 
        else:
            novalid = True
            
    else:
        form = DriverAddForm()
        formoffer = DriverAddFormOffer()
        
    context = {'cities': cities, 'form': form, 
               'formoffer': formoffer, 'novalid': novalid, 'citygeo': citygeo, 'cars':cars}
   
    return render(request, 'index.html', context)



def about(request, city):
    cities = CityPark.objects.all()
    citygeo = CityPark.objects.get(name=city)
    managers = ParkManager.objects.all()
    videoabout = VideoAbout.objects.all()
    
    novalid = None
    if request.method == "POST":
        form = DriverAddForm(request.POST)
        formquest = DriverAddFormQuest(request.POST)
        driver_phone = request.POST['phone_number']
        if formquest.is_valid():
            formquest.save()
            driver = Driver.objects.get(phone_number=driver_phone)
            driver.city = citygeo
            driver.save()
            formquest = DriverAddFormQuest()
            return redirect(request.META.get('HTTP_REFERER'))
        elif form.is_valid():
            form.save()
            driver = Driver.objects.get(phone_number=driver_phone)
            driver.city = citygeo
            driver.save()
            form = DriverAddForm()
            return redirect(request.META.get('HTTP_REFERER')) 
        else:
            novalid = True
    else:
        form = DriverAddForm()
        formquest = DriverAddFormQuest()
    context = {'form': form, 'novalid': novalid, 'formquest': formquest, 
               'cities': cities, 'citygeo': citygeo, 'managers': managers, 'videoabout': videoabout,}
    return render(request, 'etaxi/pageAboutUs.html', context)

def contacts(request, city):
    cities = CityPark.objects.all()
    citygeo = CityPark.objects.get(name=city)
    
    novalid = None
    if request.method == "POST":
        form = DriverAddForm(request.POST)
        driver_phone = request.POST['phone_number']
        if form.is_valid():
            form.save()
            driver = Driver.objects.get(phone_number=driver_phone)
            driver.city = citygeo
            driver.save()
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









   


