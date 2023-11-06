from django.contrib import admin
from .models import *
# Register your models here.

class TaxiCarManyInline(admin.TabularInline):
    model = TaxiCarMany
    extra = 1
    verbose_name_plural = "Автомобили"
    verbose_name = "Автомобиль"
class CarParkAdmin(admin.ModelAdmin):
    inlines = [TaxiCarManyInline]
   
admin.site.register(City)
admin.site.register(Driver)
admin.site.register(TaxiCar)
admin.site.register(ParkManager)
admin.site.register(CarPark, CarParkAdmin)

