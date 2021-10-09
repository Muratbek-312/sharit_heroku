from django.contrib.auth import get_user_model
from django.core.mail import send_mail
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.generics import get_object_or_404, GenericAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from Accounts.serializers import RegisterSerializer, LogoutSerializer

from Accounts.tasks import send_activation_mail



class RegisterView(APIView):
    def post(self, request, *args, **kwargs):
        data = request.data
        serializer = RegisterSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            user = serializer.save()
            send_activation_mail(user)
            return Response('Аккаунт успешно создан')

class ActivationView(APIView):
    def get(self, request, activation_code):
        User = get_user_model()
        user = get_object_or_404(User, activation_code=activation_code)
        user.actination_with_code(activation_code)
        return Response('Ваш аккаунт успешно автивирован')


class LogoutView(GenericAPIView):
    serializer_class = LogoutSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response('Successfully logged out', status.HTTP_200_OK)