from django.contrib import admin
from django.urls import path, include
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title='Maps API',
        default_version='v1',
        description='Maps API'
    ), public=True
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('account/', include('Accounts.urls')),
    path('', schema_view.with_ui()),
    path('api/', include('Main.urls')),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)