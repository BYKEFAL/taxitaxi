from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
class City(models.Model):
    name = models.CharField(verbose_name='Город', max_length=200)
    
    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Города"
        verbose_name = 'Город'
        
class Driver(models.Model):
    name = models.CharField(verbose_name='Клиент', max_length=40, blank=False, null=False)
    phone_number = PhoneNumberField(unique=True, null=False, blank=False)
    dateCreation = models.DateTimeField(auto_now_add=True)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    
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
    regNumber = models.CharField(verbose_name='Рег. номер', max_length=10, blank=False, null=False)
    yearIssu = models.IntegerField(verbose_name='Год выпуска')
    status = models.BooleanField(default=False)
    driver = models.ManyToManyField(Driver, through='DriverMany')
    discription = models.TextField()
    image = models.ImageField(upload_to='images/cars/%Y-%m-%d/')
    dateCreation = models.DateTimeField(auto_now_add=True)
    
class ParkManager(models.Model):
    firtName = models.CharField(max_length=40, blank=False, null=False)
    lastName = models.CharField(max_length=40)
    phone_number = PhoneNumberField(unique=True, null=False, blank=False)
    email = models.EmailField()
    dateCreation = models.DateTimeField(auto_now_add=True)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    
class CarPark(models.Model):
    parkManager = models.ForeignKey(ParkManager, on_delete=models.CASCADE)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    address = models.TextField()
    phone_number = PhoneNumberField(unique=True)
    taxiCar = models.ManyToManyField(TaxiCar, through='TaxiCarMany')
    dateCreation = models.DateTimeField(auto_now_add=True)
    
class TaxiCarMany(models.Model):
    carParkThrough = models.ForeignKey(CarPark, on_delete=models.CASCADE)
    taxiCarThrough = models.ForeignKey(TaxiCar, on_delete=models.CASCADE) 
    
class DriverMany(models.Model):
    taxiCarThrough = models.ForeignKey(TaxiCar, on_delete=models.CASCADE)
    driverThrough = models.ForeignKey(Driver, on_delete=models.CASCADE)
    
    
