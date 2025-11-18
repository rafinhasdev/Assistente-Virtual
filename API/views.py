from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from accounts.models import Usuarios
from accounts.serializers import UsuariosSerializer, UsuariosSlimSerializerGet

from .models import Credenciais
from .serializers import CredenciaisSerializer, CredentiaisView, TelefoneCheckSerializer, TelefoneUpdateSerializer


class CredenciaisCreateView(generics.CreateAPIView):
    queryset = Credenciais.objects.all()
    serializer_class = CredenciaisSerializer


class CredenciaisListView(generics.ListAPIView):
    queryset = Credenciais.objects.all()
    serializer_class = CredentiaisView


class UsuariosListView(generics.ListAPIView):
    queryset = Usuarios.objects.all()
    serializer_class = UsuariosSerializer


class UsuariosSlimListView(generics.ListAPIView):
    queryset = Usuarios.objects.all()
    serializer_class = UsuariosSlimSerializerGet


class UsuariosDeleteView(generics.DestroyAPIView):
    queryset = Usuarios.objects.all()
    serializer_class = UsuariosSerializer
    lookup_field = "pk"

class CheckTelefoneView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = TelefoneCheckSerializer(data=request.data)
        if serializer.is_valid():
            numero = serializer.validated_data['numero']
            
            try:
                usuario = Usuarios.objects.get(numero=numero)
            
            except Usuarios.DoesNotExist:
                return Response(
                    {
                        "exists": False, "usuario": None
                    }, status=status.HTTP_200_OK
                )
        
            usuario_serializer = UsuariosSerializer(usuario)

            return Response(
                {
                    "exists": True, "usuario": usuario_serializer.data
                }, status=status.HTTP_200_OK
            )

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UpdateTelefonePorMatriculaView(APIView):
    def get(self, request, matricula, *args, **kwargs):
        try:
            usuario = Usuarios.objects.get(username=matricula)
        except Usuarios.DoesNotExist:
            return Response({"detail": "Usuário não encontrado."}, status=404)

        return Response(UsuariosSerializer(usuario).data)

    def patch(self, request, matricula, *args, **kwargs):
        serializer = TelefoneUpdateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        try:
            usuario = Usuarios.objects.get(username=matricula)
        except Usuarios.DoesNotExist:
            return Response({"detail": "Usuário não encontrado."}, status=404)

        usuario.numero = serializer.validated_data["numero"]
        usuario.save()

        return Response(
            {"detail": "Telefone atualizado com sucesso.",
             "usuario": UsuariosSerializer(usuario).data},
            status=200
        )

