from django.contrib.auth.models import User
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    """
    Serializador para la informacion de User
    """
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')


class CreatUserSerializer(serializers.ModelSerializer):
    """
    Serializador para CREAR un User
    """
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password')

    def create(self, validated_data):
        """
        Sobre escribo el metodo create para que encripte la contraseña
        :param validated_data:
        :return:
        """
        user = User(**validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user
