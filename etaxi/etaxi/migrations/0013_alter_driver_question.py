# Generated by Django 4.2.7 on 2023-11-21 18:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('etaxi', '0012_alter_driver_city_alter_driver_confirmation_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='driver',
            name='question',
            field=models.CharField(blank=True, max_length=500, null=True, verbose_name='Вопрос клиента'),
        ),
    ]
