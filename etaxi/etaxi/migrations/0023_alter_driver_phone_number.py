# Generated by Django 4.2.7 on 2023-11-26 19:11

from django.db import migrations
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('etaxi', '0022_alter_driver_phone_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='driver',
            name='phone_number',
            field=phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None, unique=True, verbose_name='Телефон'),
        ),
    ]
