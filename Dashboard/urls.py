from django.urls import path, include
from .views import *

urlspatterns = [
    ##path('', index, name='index'),
    path('backlogs/', BacklogsListView.as_view(), name='backlogs_list'),
    path('backlogs/<int:pk>/', BacklogsDetailView.as_view(), name='backlogs_detail'),
    path('backlogs/create/', BacklogsCreateView.as_view(), name='backlogs_create'),
    path('backlogs/<int:pk>/update/', BacklogsUpdateView.as_view(), name='backlogs_update'),
    path('backlogs/<int:pk>/delete/', BacklogsDeleteView.as_view(), name='backlogs_delete'),
    path('support/', SupportMensagensListView.as_view(), name='support_list'),
    path('support/<int:pk>/', SupportMensagensDetailView.as_view(), name='support_detail'),
    path('support/create/', SupportMensagensCreateView.as_view(), name='support_create'),
    path('support/<int:pk>/update/', SupportMensagensUpdateView.as_view(), name='support_update'),
    path('support/<int:pk>/delete/', SupportMensagensDeleteView.as_view(), name='support_delete'),
    path('usuarios/', UsuariosListView.as_view(), name='usuarios_list'),
    path('usuarios/<int:pk>/', UsuariosDetailView.as_view(), name='usuarios_detail'),
    path('usuarios/create/', UsuariosCreateView.as_view(), name='usuarios_create'),
    path('usuarios/<int:pk>/update/', UsuariosUpdateView.as_view(), name='usuarios_update'),
    path('usuarios/<int:pk>/delete/', UsuariosDeleteView.as_view(), name='usuarios_delete'),
]

    
    