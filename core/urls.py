"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf import settings
from django.urls import path
from django.conf.urls.static import static
from app.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name="index"),
    path('login/', login, name="login"),
    path('dashboard/', dashboard, name="dashboard"),

    path('dashboard/support/', support_listar, name="support"), #Funciona
    path('dashboard/support_criar/', support_criar, name="support_criar"), #Falta criar
    path('dashboard/support_editar/<int:pk>/', support_editar, name="support_editar"), #Falta criar
    path('dashboard/support_remover/<int:pk>/', support_remover, name="support_remover"), #Funciona

    path('dashboard/usuarios', usuarios, name="usuarios"), #Funciona
    path('dashboard/usuarios_detail/<int:pk>', usuario_detail, name="usuario_detail"), #Falta criar
    path('dashboard/usuarios_criar', usuarios_criar, name="usuarios_criar"), #Falta criar
    path('dashboard/usuarios_editar/<int:pk>/', usuarios_editar, name="usuarios_editar"), #Falta criar
    path('dashboard/usuarios_remover/<int:pk>/', usuarios_remover, name="usuarios_remover"), #Funciona
    
    path('dashboard/backlogs/', backlogs, name="backlogs"), #Corrigir o erro de redicionamento
    path('dashboard/backlogs_criar', backlogs_criar, name="backlogs_criar"), #Funciona
    path('dashboard/backlogs_editar/<int:pk>/', backlogs_editar, name="backlogs_editar"), #Funciona
    path('dashboard/backlogs_remover/<int:pk>/', backlogs_remover, name="backlogs_remover"), #Funciona

    path('about/', about, name="about"),
    path('backlogs/', listar_backlogs, name="listar_backlogs")
    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)