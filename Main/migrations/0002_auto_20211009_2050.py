# Generated by Django 3.2.8 on 2021-10-09 14:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='mapsmodel',
            name='maps_url',
            field=models.URLField(blank=True, null=True, verbose_name='url'),
        ),
        migrations.AlterField(
            model_name='favorite',
            name='maps',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='favorites', to='Main.mapsmodel', verbose_name='Карта пути'),
        ),
        migrations.AlterField(
            model_name='favorite',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='favorites', to=settings.AUTH_USER_MODEL, verbose_name='Пользоваеть'),
        ),
    ]
