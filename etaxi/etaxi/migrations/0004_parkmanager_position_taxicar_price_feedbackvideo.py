# Generated by Django 4.2.7 on 2023-11-07 18:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('etaxi', '0003_alter_carpark_options_alter_parkmanager_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='parkmanager',
            name='position',
            field=models.CharField(default='директор', max_length=200, verbose_name='Должность'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='taxicar',
            name='price',
            field=models.IntegerField(default=100, verbose_name='Цена'),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='FeedbackVideo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='название видео')),
                ('video', models.FileField(upload_to='video/feedback/%Y-%m-%d/', verbose_name='Видео')),
                ('dateCreation', models.DateTimeField(auto_now_add=True)),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='etaxi.city', verbose_name='Город')),
            ],
            options={
                'verbose_name': 'Видеоотзыв',
                'verbose_name_plural': 'Видеоотзывы',
            },
        ),
    ]