# Generated by Django 4.2.7 on 2023-11-26 13:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('etaxi', '0017_taxicar_enginecapacity_taxicar_geartype'),
    ]

    operations = [
        migrations.AlterField(
            model_name='taxicar',
            name='engineCapacity',
            field=models.FloatField(max_length=100, verbose_name='Обьем двигателя'),
        ),
    ]
