from .models import MapsModel, Favorite
from rest_framework import serializers
from .models import MapsModel, Favorite
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username']


class FavoriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Favorite
        fields = ['id', 'user', 'maps']


class MapsSerializer(serializers.ModelSerializer):

    class Meta:
        model = MapsModel
        fields = ['id', 'user', 'title', 'from_location', 'maps_url', 'to_location', 'is_active', 'choices_types', 'days_on_week',
                  'date_time', 'date_time_end', 'notes']


