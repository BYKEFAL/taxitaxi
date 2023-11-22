from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from embed_video.fields import EmbedVideoField
from .validators import DriverNameValidator

# Create your models here.
class City(models.Model):
    name = models.CharField(verbose_name='Город', max_length=200)
    
    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Города"
        verbose_name = 'Город'
        
class CityPark(models.Model):
    name = models.CharField(verbose_name='Город', max_length=200)
    latitude = models.FloatField(verbose_name='Широта', null=False)
    longitude = models.FloatField(verbose_name='Долгота', null=False)
    
    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Города"
        verbose_name = 'Город'
        ordering = ['name']
        
class Driver(models.Model):
    name = models.CharField(validators=[DriverNameValidator], verbose_name='Водитель', max_length=40, blank=False, null=False)
    phone_number = PhoneNumberField(verbose_name='Телефон', unique=True, null=False, blank=False)
    dateCreation = models.DateTimeField(auto_now_add=True)
    city = models.ForeignKey(CityPark, on_delete=models.CASCADE, verbose_name='Город', blank=True, null=True,)
    confirmation = models.BooleanField(verbose_name='Соглашение на обработку получено', default=True)
    question = models.TextField(max_length=500, blank=True, null=True, verbose_name='Вопрос клиента' )
    
    class Meta:
        verbose_name_plural = "Водители"
        verbose_name = 'Водитель'
        
    def __str__(self):
        return f'{self.name} ({self.phone_number})'
    
class TaxiCar(models.Model):
    SEDAN = 'SD'
    HATCHBACK = 'HT'
    LIFTBACK = 'LF'
    JEEP = 'JP'
    UNIVERSAL = 'UN'
    MINIVAN= 'MW'
    PIKUP = 'PK'

    CATEGORY_CHOICES = (
        (SEDAN, 'Седан'),
        (HATCHBACK, 'Хэтчбэк'),
        (LIFTBACK, 'Лифтбэк'),
        (JEEP, 'Джип'),
        (UNIVERSAL, 'Универсал'),
        (MINIVAN, 'Минивэн'),
        (PIKUP, 'Пикап'),
    )
    
    brand = models.CharField(verbose_name='Марка', max_length=100, blank=False, null=False)
    model = models.CharField(verbose_name='Модель', max_length=100, blank=False, null=False)
    carType = models.CharField(verbose_name='Тип Кузова', max_length=2, choices=CATEGORY_CHOICES)
    regNumber = models.CharField(verbose_name='Рег. номер', max_length=20, blank=False, null=False)
    yearIssu = models.IntegerField(verbose_name='Год выпуска')
    status = models.BooleanField(default=False, verbose_name='Занят/Свободен')
    driver = models.ManyToManyField(Driver, through='DriverMany')
    discription = models.TextField(verbose_name='Описание')
    image = models.ImageField(upload_to='images/cars/%Y-%m-%d/', verbose_name='Загрузить Фото')
    dateCreation = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания' )
    dateUpdate = models.DateTimeField(auto_now=True, verbose_name='Дата изменения', null=True )
    city = models.ForeignKey(CityPark, on_delete=models.SET_NULL, verbose_name='Город', null=True)
    price = models.IntegerField(verbose_name='Цена')
    class Meta:
        verbose_name_plural = "Автомобили"
        verbose_name = 'Автомобиль'
    
    def __str__(self):
        return f'{self.brand} {self.model} {self.regNumber} - {self.city}'
    
class ParkManager(models.Model):
    firstName = models.CharField(max_length=40, blank=False, null=False, verbose_name='Имя')
    lastName = models.CharField(max_length=40, verbose_name='Фамилия')
    phone_number = PhoneNumberField(unique=True, null=False, blank=False, verbose_name='Телефон')
    email = models.EmailField(verbose_name='Почта')
    dateCreation = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    dateUpdate = models.DateTimeField(auto_now=True, verbose_name='Дата изменения', null=True )
    city = models.ForeignKey(CityPark, on_delete=models.SET_NULL, verbose_name='Город', null=True)
    position = models.CharField(max_length=200, verbose_name='Должность')
    image = models.ImageField(upload_to='images/managers/%Y-%m-%d/', verbose_name='Загрузить Фото', null=True, blank=True)
    
    
    class Meta:
        verbose_name_plural = "Менеджеры таксопарков"
        verbose_name = 'Менеджер таксопарка'
    
    def __str__(self) -> str:
        return f'{self.firstName} {self.lastName} - {self.city}'
    
class CarPark(models.Model):
    name = models.CharField(verbose_name='название таксопарка', max_length=50, blank=False, null=False)
    parkManager = models.ForeignKey(ParkManager, on_delete=models.SET_NULL, verbose_name='Менеджер', null=True)
    city = models.ForeignKey(CityPark, on_delete=models.CASCADE, verbose_name='Город')
    address = models.TextField(verbose_name='Адрес')
    phone_number = PhoneNumberField(unique=True, verbose_name='Телефон')
    taxiCar = models.ManyToManyField(TaxiCar, through='TaxiCarMany', verbose_name='Автомобили')
    dateCreation = models.DateTimeField(auto_now_add=True)
    dateUpdate = models.DateTimeField(auto_now=True, verbose_name='Дата изменения', null=True )
    
    class Meta:
        verbose_name_plural = "Таксопарки автомобилей"
        verbose_name = 'Таксопарк автомобилей'
        
    def __str__(self):
        return f'г. {self.city}, таксопарк - {self.name}'
    
class FeedbackVideo(models.Model):
    city = models.ForeignKey(CityPark, on_delete=models.CASCADE, verbose_name='Город', null=False)
    name = models.CharField(verbose_name='Название видео', max_length=50, blank=False, null=False)
    video = models.FileField(upload_to='video/feedback/%Y-%m-%d/', verbose_name='Видеофайл',blank=True, null=True,)
    youtube = EmbedVideoField(blank=True, null=True, verbose_name='Youtube ссылка')
    dateCreation = models.DateTimeField(auto_now_add=True)
    dateUpdate = models.DateTimeField(auto_now=True, verbose_name='Дата изменения', null=True )
    
    
    class Meta:
        verbose_name_plural = "Видеоотзывы"
        verbose_name = 'Видеоотзыв'
        
    def __str__(self):
        return f'г.{self.city} {self.name}' 
    
class TaxiCarMany(models.Model):
    carParkThrough = models.ForeignKey(CarPark, on_delete=models.CASCADE)
    taxiCarThrough = models.ForeignKey(TaxiCar, on_delete=models.CASCADE, verbose_name="автомобили таксопарка") 
    
    def __str__(self):
        return ' '
    
class DriverMany(models.Model):
    taxiCarThrough = models.ForeignKey(TaxiCar, on_delete=models.CASCADE)
    driverThrough = models.ForeignKey(Driver, on_delete=models.CASCADE, verbose_name="автомобиль арендовали")
    
    def __str__(self):
        return ' '
    
    
