# Generated by Django 4.2.7 on 2023-11-07 18:58

from django.db import migrations, models
import django.db.models.deletion
import embed_video.fields


class Migration(migrations.Migration):

    dependencies = [
        ('etaxi', '0004_parkmanager_position_taxicar_price_feedbackvideo'),
    ]

    operations = [
        migrations.AddField(
            model_name='feedbackvideo',
            name='youtube',
            field=embed_video.fields.EmbedVideoField(blank=True, null=True, verbose_name='Youtube ссылка'),
        ),
        migrations.AlterField(
            model_name='drivermany',
            name='driverThrough',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='etaxi.driver', verbose_name='автомобиль арендовали'),
        ),
        migrations.AlterField(
            model_name='feedbackvideo',
            name='name',
            field=models.CharField(max_length=50, verbose_name='Название видео'),
        ),
        migrations.AlterField(
            model_name='feedbackvideo',
            name='video',
            field=models.FileField(upload_to='video/feedback/%Y-%m-%d/', verbose_name='Видеофайл'),
        ),
    ]
