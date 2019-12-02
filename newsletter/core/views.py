from django.contrib.auth.models import User
from rest_framework import viewsets

from core.serializers import UserSerializer, CreatUserSerializer
from rest_framework.permissions import AllowAny


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_permissions(self):
        """
        sobre escribimos el metodo para que podamos esntrar a
        las otras vistas
        :return:
        """
        if self.action == 'create':
            self.permission_classes = [AllowAny]
        return (permission() for permission in self.permission_classes)


    def get_serializer_class(self):
        """
        Si la accion es create usa CreatUserSerializer
        :return:
        """
        if self.action == 'create':
            return CreatUserSerializer
        return UserSerializer
