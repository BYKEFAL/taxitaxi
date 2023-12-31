# Generated by Django 4.2.7 on 2023-11-07 19:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('etaxi', '0005_feedbackvideo_youtube_alter_drivermany_driverthrough_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carpark',
            name='parkManager',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='etaxi.parkmanager', verbose_name='Менеджер'),
        ),
        migrations.AlterField(
            model_name='parkmanager',
            name='city',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='etaxi.city', verbose_name='Город'),
        ),
        migrations.AlterField(
            model_name='taxicar',
            name='city',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='etaxi.city', verbose_name='Город'),
        ),
    ]
