from django.db import models

# Create your models here.
class City(models.Model):
    name = models.CharField(verbose_name='Город', max_length=200)
    
    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Города"
        verbose_name = 'Город'