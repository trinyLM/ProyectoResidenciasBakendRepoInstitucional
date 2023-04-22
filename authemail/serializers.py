from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from autenticacion.models import CustomUser as user

class SignupSerializer(serializers.Serializer):
    """
    Don't require email to be unique so visitor can signup multiple times,
    if misplace verification email.  Handle in view.
    """
    email = serializers.EmailField(max_length=255)
    password = serializers.CharField(max_length=128)
    first_name = serializers.CharField(max_length=30, default='',
                                       required=False)
    last_name = serializers.CharField(max_length=30, default='',
                                      required=False)
    apellido_materno = serializers.CharField(max_length=100)
    matricula = serializers.CharField(max_length=8,validators=[UniqueValidator(queryset=user.objects.all())])

    def validate(self, attrs):
        if not attrs['email'].endswith("zongolica.tecnm.mx"):
            raise serializers.ValidationError(
                {"email": "solo se aceptan correos instucionales","status":"failed"})
        return attrs


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField(max_length=255)
    password = serializers.CharField(max_length=128)


class PasswordResetSerializer(serializers.Serializer):
    email = serializers.EmailField(max_length=255)


class PasswordResetVerifiedSerializer(serializers.Serializer):
    code = serializers.CharField(max_length=40)
    password = serializers.CharField(max_length=128)


class PasswordChangeSerializer(serializers.Serializer):
    password = serializers.CharField(max_length=128)


class EmailChangeSerializer(serializers.Serializer):
    email = serializers.EmailField(max_length=255)


class EmailChangeVerifySerializer(serializers.Serializer):
    email = serializers.EmailField(max_length=255)


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('id', 'email', 'first_name', 'last_name','apellido_materno','matricula')