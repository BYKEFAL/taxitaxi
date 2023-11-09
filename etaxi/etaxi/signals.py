from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Driver
from django.conf import settings


@receiver(post_save, sender=Driver)
def add_driver_to_bitrix(sender, instance, created, **kwargs):

    # Если водитель нажал форму отправить, то автоматом добавился в базу
    if created:
       #если добавился то отправляем данные в битрих
       #сдесь будет отправка через API
       print(instance.phone_number)
       
    if True:
       #сдесь можно допом отправить письмо на почту но это по желанию.
       pass