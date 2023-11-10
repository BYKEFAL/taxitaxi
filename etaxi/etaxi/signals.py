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
        fields = ['id', 'name', 'phone_number']


@receiver(post_save, sender=Driver)
def add_driver_to_bitrix(sender, instance, created, **kwargs):
    # вебхук
    bx24 = Bitrix24('https://example.bitrix24.com/rest/1/33olqeits4avuyqu') 
    # Если водитель нажал форму отправить, то автоматом добавился в базу, и залетел в битрих24
    if created:
       serializer = DriverSerializer(instance)
       driver_city = instance.city.name
       if serializer:
          driver_bitrix = serializer.data
          try:
             response = bx24.callMethod('crm.lead.add', fields={
                  'TITLE': 'Сайт ETAXI заявка',
                  'NAME': driver_bitrix['name'],
                  'SOURCE_ID': driver_bitrix['id'],
                  'ADDRESS_CITY': driver_city,
                  'PHONE': [{'VALUE': driver_bitrix['phone_number'], 'VALUE_TYPE': 'WORK'}],
                  
               })
          except BitrixError as message:
              print(message)
          return Response(response.json())
    return Response(serializer.errors, status=400)
 
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
   
   
   
         