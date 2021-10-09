from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView, TokenObtainPairView
from django.views.decorators.csrf import csrf_exempt
from Accounts.views import RegisterView, ActivationView, LogoutView


urlpatterns = [
    path('register/', RegisterView.as_view()),
    path('activate/<str:activation_code>/', ActivationView.as_view()),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
	path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('logout/', csrf_exempt(LogoutView.as_view()), name='logout'),
]