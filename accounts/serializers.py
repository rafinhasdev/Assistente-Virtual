from rest_framework import serializers
from .models import Usuarios

class UsuariosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuarios
        fields = '__all__'

class UsuariosSlimSerializerGet(serializers.ModelSerializer):
    class Meta:
        model = Usuarios
        fields = ('matricula', 'numero', 'nome', 'sobrenome')