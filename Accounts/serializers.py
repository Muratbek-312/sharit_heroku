from django.contrib.auth import authenticate
from django.utils.translation import gettext_lazy as _
from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.exceptions import TokenError
from rest_framework_simplejwt.tokens import RefreshToken


User = get_user_model()

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('email', )



class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(min_length=3, required=True)
    password_confirm = serializers.CharField(min_length=3, required=True)
    class Meta:
        model = User
        fields = ('email', 'password', 'password_confirm', 'name')


    def validate_email(self, value):
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError('Пользователь с таким email уже зарегистрирован')
        return value

    def validate(self, attrs):
        password = attrs.get('password')
        password_confirm = attrs.pop('password_confirm', None)
        if password != password_confirm:
            raise serializers.ValidationError('Пароли не совпадают')
        return attrs


class LogoutSerializer(serializers.Serializer):
    refresh = serializers.CharField()

    def validate(self, attrs):
        print('333333333')
        self.token = attrs.get('refresh')
        print(self.token , '222222222')
        return attrs

    def save(self, **kwargs):
        try:
            RefreshToken(self.token).blacklist()
        except TokenError:
            self.fail('Incorrect token')