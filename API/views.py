from rest_framework import generics
from .models import Credenciais
from .serializers import CredenciaisSerializer, CredentiaisView
from app.models import Usuarios
from app.serializers import UsuariosSerializer, UsuariosSlimSerializerGet


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


# Create your views here.
