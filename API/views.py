from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from accounts.models import Usuarios
from accounts.serializers import UsuariosSerializer, UsuariosSlimSerializerGet

from .models import Credenciais
from .serializers import (
    CredenciaisSerializer,
    CredenciaisRetrieveSerializer,
    TelefoneCheckSerializer,
    CredenciaisUpsertSerializer,
)

class CredenciaisUpsertView(generics.GenericAPIView):
    serializer_class = CredenciaisUpsertSerializer

    def post(self, request, username):

        try:
            usuario = Usuarios.objects.get(username=username)
        except Usuarios.DoesNotExist:
            return Response({"error": "Usuário não encontrado"}, status=404)

        credenciais = Credenciais.objects.filter(usuario=usuario).first()

        serializer = self.get_serializer(
            instance=credenciais,
            data=request.data,
            partial=True 
        )

        serializer.is_valid(raise_exception=True)

        if credenciais:
            serializer.save()
            return Response(
                {"message": "Credenciais atualizadas com sucesso", "data": serializer.data},
                status=status.HTTP_200_OK,
            )

        serializer.save(usuario=usuario)
        return Response(
            {"message": "Credenciais criadas com sucesso", "data": serializer.data},
            status=status.HTTP_201_CREATED,
        )




class CredenciaisCreateView(generics.CreateAPIView):
    queryset = Credenciais.objects.all()
    serializer_class = CredenciaisSerializer


class CredenciaisRetrieveView(generics.GenericAPIView):
    serializer_class = CredenciaisRetrieveSerializer

    def get(self, request, username):
        try:
            usuario = Usuarios.objects.get(username=username)
        except Usuarios.DoesNotExist:
            return Response({"error": "Usuário não encontrado"}, status=404)

        credenciais = Credenciais.objects.filter(usuario=usuario).first()
        if not credenciais:
            return Response({"error": "Credenciais não encontradas"}, status=404)

        serializer = self.get_serializer(credenciais)
        return Response(serializer.data, status=200)


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
            numero = serializer.validated_data["numero"]

            try:
                usuario = Usuarios.objects.get(numero=numero)

            except Usuarios.DoesNotExist:
                return Response(
                    {"exists": False, "usuario": None}, status=status.HTTP_200_OK
                )

            usuario_serializer = UsuariosSerializer(usuario)

            return Response(
                {"exists": True, "usuario": usuario_serializer.data},
                status=status.HTTP_200_OK,
            )

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TelefoneView(generics.GenericAPIView):
    serializer_class = TelefoneCheckSerializer

    def get_user(self, username):
        try:
            return Usuarios.objects.get(username=username)
        except Usuarios.DoesNotExist:
            return None

    def get(self, request, username):
        user = self.get_user(username)
        if not user:
            return Response({"error": "Usuário não encontrado"}, status=404)

        return Response({"numero": user.numero}, status=200)

    def post(self, request, username):
        """
        Cria ou atualiza o número do usuário.
        """
        user = self.get_user(username)
        if not user:
            return Response({"error": "Usuário não encontrado"}, status=404)

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user.numero = serializer.validated_data["numero"]
        user.save()

        return Response(
            {"message": "Número salvo/atualizado com sucesso", "numero": user.numero},
            status=200
        )

    def put(self, request, username):
        return self.post(request, username)

    def patch(self, request, username):
        return self.post(request, username)