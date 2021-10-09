from django.db import models
from django.contrib.auth.models import User

Ride_Choices = (
    ('WALK', "Пешком"),
    ('BUS', "На автобусе"),
    ('TAXI', "На такси"),
    ('CAR', "На машине")
)

Days_Choices = (
    ('1', "Понедельник"),
    ('2', "Вторник"),
    ('3', "Среда"),
    ('4', "Четверг"),
    ('5', "Пятница"),
    ('6', "Суббота"),
    ('7', "Воскресенье")
)


class MapsModel(models.Model):

    title = models.CharField(verbose_name='Краткое описание', max_length=155, blank=True)
    from_location = models.CharField(verbose_name='От куда', max_length=255, db_index=True)
    to_location = models.CharField(verbose_name='До куда', max_length=255, db_index=True)
    maps_url = models.URLField(verbose_name='url', blank=True, null=True)
    is_active = models.BooleanField(default=True, verbose_name='Активен')
    choices_types = models.CharField(max_length=4, choices=Ride_Choices, default='CAR', verbose_name='Выбор поездки')
    days_on_week = models.CharField(max_length=7, choices=Days_Choices, default='1',
                                    verbose_name='Дни недель')
    date_time = models.DateTimeField(auto_now=True, verbose_name='Дата когда будет идти маршрут')
    date_time_end = models.DateTimeField(auto_now=True, verbose_name='Дата когда закончиться маршрут')
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь', related_name='maps')
    notes = models.TextField(verbose_name='Описание пути', blank=True, null=True)


class Favorite(models.Model):
    user = models.ForeignKey(User, verbose_name='Пользоваеть', related_name='favorites', on_delete=models.CASCADE)
    maps = models.ForeignKey(MapsModel, verbose_name='Карта пути', related_name='favorites', on_delete=models.CASCADE)






