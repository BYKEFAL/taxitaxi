# Generated by Django 4.2.7 on 2023-11-22 20:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('etaxi', '0014_alter_driver_question'),
    ]

    operations = [
        migrations.AddField(
            model_name='citypark',
            name='latitude',
            field=models.FloatField(null=True, verbose_name='Широта'),
        ),
        migrations.AddField(
            model_name='citypark',
            name='longitude',
            field=models.FloatField(null=True, verbose_name='Долгота'),
        ),
    ]
