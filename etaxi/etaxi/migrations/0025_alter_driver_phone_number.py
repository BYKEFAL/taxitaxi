# Generated by Django 4.2.7 on 2023-11-28 11:43

from django.db import migrations
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('etaxi', '0024_videoabout'),
    ]

    operations = [
        migrations.AlterField(
            model_name='driver',
            name='phone_number',
            field=phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None, verbose_name='Телефон'),
        ),
    ]
