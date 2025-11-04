from rest_framework import serializers
from .models import Credenciais
from accounts.models import Usuarios
from accounts.serializers import UsuariosSerializer

class CredenciaisSerializer(serializers.ModelSerializer):
    usuario = UsuariosSerializer()

    class Meta:
        model = Credenciais
        fields = '__all__'

    def create(self, validated_data):
        usuario_data = validated_data.pop('usuario')
        usuario, _ = Usuarios.objects.get_or_create(
            matricula=usuario_data.get('matricula'),
            defaults=usuario_data
        )
        credencial = Credenciais.objects.create(usuario=usuario, **validated_data)
        return credencial

class CredentiaisView(serializers.ModelSerializer):
    class Meta:
        model = Credenciais
        fields = ['suap_token', 'bearer']