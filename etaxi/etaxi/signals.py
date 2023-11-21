from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Driver
from django.conf import settings
from rest_framework import serializers
from rest_framework.response import Response
from bitrix24 import *

class DriverSerializer(serializers.ModelSerializer):
    class Meta:
        model = Driver
        fields = ['id', 'name', 'phone_number', 'question']


# @receiver(post_save, sender=Driver)
# def add_driver_to_bitrix(sender, instance, created, **kwargs):
#     # вставьте свой вебхук
#     bx24 = Bitrix24('https://b24-4sb7sd.bitrix24.ru/rest/1/n66mcst4qnuq9yl6/') 
#     # Если водитель нажал форму отправить, то автоматом добавился в базу, и залетел в битрих24
#     if created:
#        serializer = DriverSerializer(instance)
#        driver_city = instance.city.name
#        if serializer:
#           driver_bitrix = serializer.data
#           try:
#              response = bx24.callMethod('crm.lead.add', fields={
#                   'TITLE': 'Новый лид от сайта ETAXI',
#                   'NAME': driver_bitrix['name'],
#                   'LAST_NAME': driver_bitrix['name'] + ' ETAXI',
#                   'COMPANY_TITLE': driver_bitrix['name'] + f' из города {driver_city}',
#                   'SOURCE_ID': 'WEB',
#                   'SOURCE_DESCRIPTION': 'Вопрос клиента - ' + driver_bitrix['question'],
#                   'STATUS_ID': 'NEW',
#                   'POST': 'Клиент Etaxi',
#                   'ADDRESS_CITY': f'город {driver_city}',
#                   'OPENED': 'Y',
#                   'PHONE': [{'VALUE': driver_bitrix['phone_number'], 'VALUE_TYPE': 'WORK'}],
#                   'WEB': [{'VALUE': 'https://вашдоменсайта.ru', 'VALUE_TYPE': 'OTHER'}],
#                   'ORIGIN_ID': driver_bitrix['id'],
#                })
#           except BitrixError as message:
#               print(message)
 
# some local tests
# class Driver:
#     def __init__(self, name, phone):
#         self.name = name
#         self.phone_number = phone
 
# def decode():
#    model = Driver.objects.get(pk=1)
#    city = model.city.name
#    serializer = DriverSerializer(model)
#    driver_bitrix = serializer.data
#    print(driver_bitrix, city)

# def getlead(pk):
#    bx24 = Bitrix24('https://b24-4sb7sd.bitrix24.ru/rest/1/n66mcst4qnuq9yl6/')
#    response = bx24.callMethod('crm.lead.get', id=pk)
#    return response

# заготовочка для другого места.
# <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>
# <script>
# $(document).ready(function(){
#     setTimeout(function(){
#        location.reload(true);
#        alert("The page will now refresh");
#     }, 60000);  
# });
# </script>

   
         