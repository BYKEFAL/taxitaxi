from django.shortcuts import render, HttpResponse
import requests
import json
from ipware import get_client_ip
# from django.contrib.gis.geoip2 import GeoIP2
from dadata import Dadata

# Определение города на Русском по IP
token = "d1b7f800e7beb52dbc7b32f8f140808fe8e7bfaa"
dadata = Dadata(token)

def home(request):
    client_ip, is_routable = get_client_ip(request)
    client_ip = '176.59.144.81' #Тестовый IP не забыть удалить
    response = dadata.iplocate(client_ip)['data']['city']
    print(client_ip)
    print(response)
    
    return HttpResponse(f'WELCOME {client_ip} {response}')

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

'''
Определение города через Geoip2
def home(request):
   client_ip, is_routable = get_client_ip(request)
   if client_ip is not None:
    g = GeoIP2()
    try:
        location = g.city(client_ip)['city']
    except:
        location = {'Локация': 'нет данных'}
   
   print(client_ip)
   return HttpResponse(f'WELCOME {client_ip} {location}')
'''




   


