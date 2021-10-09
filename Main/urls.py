from rest_framework import routers
from .views import MapsViewSet
from django.urls import path, include

router = routers.DefaultRouter()
router.register('maps', MapsViewSet)

urlpatterns = [
    path('', include(router.urls))
]

