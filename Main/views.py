from django.shortcuts import render
from rest_framework import viewsets
from .models import MapsModel, Favorite
from .serializers import MapsSerializer


class MapsViewSet(viewsets.ModelViewSet):
    queryset = MapsModel.objects.all()
    serializer_class = MapsSerializer
