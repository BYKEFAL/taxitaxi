# Generated by Django 4.2.7 on 2023-11-26 15:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('etaxi', '0020_parkmanager_discription'),
    ]

    operations = [
        migrations.AddField(
            model_name='parkmanager',
            name='thirdName',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Отчесвто'),
        ),
        migrations.AlterField(
            model_name='parkmanager',
            name='firstName',
            field=models.CharField(max_length=100, verbose_name='Имя'),
        ),
        migrations.AlterField(
            model_name='parkmanager',
            name='lastName',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Фамилия'),
        ),
    ]