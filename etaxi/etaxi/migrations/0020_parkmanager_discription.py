# Generated by Django 4.2.7 on 2023-11-26 15:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('etaxi', '0019_alter_taxicar_cartype_alter_taxicar_discription_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='parkmanager',
            name='discription',
            field=models.TextField(blank=True, null=True, verbose_name='Описание'),
        ),
    ]
