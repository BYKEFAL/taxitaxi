from django.contrib import admin
from .models import *
from django.utils.safestring import mark_safe
# Register your models here.
admin.site.site_title = 'Админ панель сайта ETAXI'
admin.site.site_header = 'Админ панель сайта ETAXI'

class TaxiCarManyInline(admin.TabularInline):
    model = TaxiCarMany
    extra = 1
    verbose_name_plural = "Автомобили"
    verbose_name = "Автомобиль"
    
class CarParkAdmin(admin.ModelAdmin):
    inlines = [TaxiCarManyInline]
    list_filter = ('city',)
    list_per_page = 10
    
class DriverManyInline(admin.TabularInline):
    model = DriverMany
    extra = 1
    verbose_name_plural = "Водители"
    verbose_name = "Водитель"
    
class TaxiCarAdmin(admin.ModelAdmin):
    inlines = [DriverManyInline]
    list_display = ('get_photo', 'brand', 'model', 'carType', 'regNumber', 'yearIssu', 'status', 'price', 'city',)
    list_filter = ('city',)
    list_display_links = ('brand', 'get_photo')
    search_fields = ('brand', 'model', 'carType', 'regNumber', 'yearIssu', 'price',)
    #порядок полей именно в форме редактирования
    fields = ('brand', 'model', 'gearType', 'engineCapacity', 'yearIssu', 'city', 'get_photo2', 'carType', 'regNumber', 'status', 'price', 
               'image',  'discription', 'dateUpdate', 'dateCreation', )
    #для добавления не редактируемых полей
    readonly_fields = ('dateCreation', 'dateUpdate', 'get_photo2',)
    save_on_top = True
    list_per_page = 10
    save_as = True

    def get_photo(self, object):
        if object.image:
            return mark_safe(f"<img src='{object.image.url}' width=50>")
        else:
            return 'Нет фото'
        
    def get_photo2(self, object):
        if object.image:
            return mark_safe(f"<img src='{object.image.url}' width=250>")
        else:
            return 'Нет фото'
        
    get_photo.short_description = 'Фото'
    get_photo2.short_description = 'Фото'
    
class ParkManagerAdmin(admin.ModelAdmin):
    list_display =('get_photo', 'firstName', 'lastName', 'city',)
    list_display_links = ('get_photo', 'firstName', )
    search_fields = ('firstName', 'lastName', 'phone_number', 'email', 'position',)
    list_filter = ('city',)
    fields = ('get_photo2', 'lastName', 'firstName', 'thirdName', 'position', 'discription', 'phone_number', 'email', 'city', 'image', 'dateCreation', 'dateUpdate',  )
    readonly_fields = ('dateCreation', 'dateUpdate', 'get_photo2',)
    save_on_top = True
    list_per_page = 10
    
    def get_photo(self, object):
        if object.image:
            return mark_safe(f"<img src='{object.image.url}' width=50>") 
        else:
            return 'Нет фото'   
        
    def get_photo2(self, object):
        if object.image:
            return mark_safe(f"<img src='{object.image.url}' width=250>")
        else:
            return 'Нет фото' 
    
    get_photo.short_description = 'Фото'
    get_photo2.short_description = 'Фото'
    
   
class DriverAdmin(admin.ModelAdmin):
    list_per_page = 10
    
   
admin.site.register(CityPark)
admin.site.register(Driver, DriverAdmin)
admin.site.register(TaxiCar, TaxiCarAdmin)
admin.site.register(ParkManager, ParkManagerAdmin)
admin.site.register(CarPark, CarParkAdmin)
admin.site.register(VideoAbout)
admin.site.register(FeedbackVideo)




