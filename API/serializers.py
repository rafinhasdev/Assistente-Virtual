from rest_framework import serializers

from accounts.models import Usuarios
from accounts.serializers import UsuariosSerializer

from .models import Credenciais


class CredenciaisSerializer(serializers.ModelSerializer):
    usuario = UsuariosSerializer()

    class Meta:
        model = Credenciais
        fields = "__all__"

    def create(self, validated_data):
        usuario_data = validated_data.pop("usuario")
        usuario, _ = Usuarios.objects.get_or_create(
            matricula=usuario_data.get("matricula"), defaults=usuario_data
        )
        credencial = Credenciais.objects.create(usuario=usuario, **validated_data)
        return credencial

class CredenciaisUpsertSerializer(serializers.ModelSerializer):
    class Meta:
        model = Credenciais
        fields = ["suap_token", "bearer"]

    def update(self, instance, validated_data):
        for attr, value in validated_data.items():
            setattr(instance, attr, value)

        instance.save()
        return instance

class CredenciaisRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Credenciais
        fields = ["suap_token", "bearer"]


class TelefoneCheckSerializer(serializers.Serializer):
    numero = serializers.CharField(required=True)

