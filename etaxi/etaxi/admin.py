from django.contrib import admin
from .models import *
from django.utils.safestring import mark_safe
# Register your models here.

class TaxiCarManyInline(admin.TabularInline):
    model = TaxiCarMany
    extra = 1
    verbose_name_plural = "Автомобили"
    verbose_name = "Автомобиль"
class CarParkAdmin(admin.ModelAdmin):
    inlines = [TaxiCarManyInline]
    
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
    fields = ('brand', 'model', 'carType', 'regNumber', 'yearIssu', 'status', 'price', 'city', 'get_photo2', 'image',  'discription', 'dateUpdate', 'dateCreation',   )
    #для добавления не редактируемых полей
    readonly_fields = ('dateCreation', 'dateUpdate', 'get_photo', 'get_photo2',)
    save_on_top = True
    # list_editable = ('price',)
    # prepopulated_fields = 
    def get_photo(self, object):
        if object.image:
            return mark_safe(f"<img src='{object.image.url}' width=50>")
        
    def get_photo2(self, object):
        if object.image:
            return mark_safe(f"<img src='{object.image.url}' width=250>")
        
    get_photo.short_description = 'Фото'
    get_photo2.short_description = 'Фото'
   
admin.site.register(CityPark)
admin.site.register(Driver)
admin.site.register(TaxiCar, TaxiCarAdmin)
admin.site.register(ParkManager)
admin.site.register(CarPark, CarParkAdmin)
admin.site.register(FeedbackVideo)

admin.site.site_title = 'Админ панель сайта ETAXI'
admin.site.site_header = 'Админ панель сайта ETAXI'

