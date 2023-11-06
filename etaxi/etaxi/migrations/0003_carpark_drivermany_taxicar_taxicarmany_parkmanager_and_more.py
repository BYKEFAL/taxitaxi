# Generated by Django 4.2.7 on 2023-11-06 16:37

from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('etaxi', '0002_alter_city_options_driver'),
    ]

    operations = [
        migrations.CreateModel(
            name='CarPark',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.TextField()),
                ('phone_number', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None, unique=True)),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='etaxi.city')),
            ],
        ),
        migrations.CreateModel(
            name='DriverMany',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('driverThrough', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='etaxi.driver')),
            ],
        ),
        migrations.CreateModel(
            name='TaxiCar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.CharField(max_length=100, verbose_name='Марка')),
                ('model', models.CharField(max_length=100, verbose_name='Модель')),
                ('carType', models.CharField(choices=[('SD', 'Седан'), ('HT', 'Хэтчбэк'), ('LF', 'Лифтбэк'), ('JP', 'Джип'), ('UN', 'Универсал'), ('MW', 'Минивэн'), ('PK', 'Пикап')], max_length=2, verbose_name='Тип Кузова')),
                ('regNumber', models.CharField(max_length=10, verbose_name='Рег. номер')),
                ('yearIssu', models.IntegerField(verbose_name='Год выпуска')),
                ('status', models.BooleanField(default=False)),
                ('discription', models.TextField()),
                ('image', models.ImageField(upload_to='images/cars/%Y-%m-%d/')),
                ('dateCreation', models.DateTimeField(auto_now_add=True)),
                ('driver', models.ManyToManyField(through='etaxi.DriverMany', to='etaxi.driver')),
            ],
        ),
        migrations.CreateModel(
            name='TaxiCarMany',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('carParkThrough', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='etaxi.carpark')),
                ('taxiCarThrough', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='etaxi.taxicar')),
            ],
        ),
        migrations.CreateModel(
            name='ParkManager',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firtName', models.CharField(max_length=40)),
                ('lastName', models.CharField(max_length=40)),
                ('phone_number', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None, unique=True)),
                ('email', models.EmailField(max_length=254)),
                ('dateCreation', models.DateTimeField(auto_now_add=True)),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='etaxi.city')),
            ],
        ),
        migrations.AddField(
            model_name='drivermany',
            name='taxiCarThrough',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='etaxi.taxicar'),
        ),
        migrations.AddField(
            model_name='carpark',
            name='parkManager',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='etaxi.parkmanager'),
        ),
        migrations.AddField(
            model_name='carpark',
            name='taxiCar',
            field=models.ManyToManyField(through='etaxi.TaxiCarMany', to='etaxi.taxicar'),
        ),
    ]
