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
    path('support/', support, name="support"),
    path('support/support_listar/', support_listar, name="support_listar"),
    path('support/support_criar/', support_criar, name="support_criar"),
    path('support/support_editar/<int:pk>/', support_editar, name="support_editar"),
    path('support/support_remover/<int:pk>/', support_remover, name="support_remover"),

    path('backlogs/', att_backlogs, name="backlogs"),
    path('dashboard/backlogs/', dashboard, name="backlogs"),
    path('about/', about, name="about"),
    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)