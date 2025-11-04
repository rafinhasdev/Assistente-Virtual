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
from django.urls import path, include
from django.conf.urls.static import static
from rest_framework.routers import DefaultRouter
from app.views import *


urlpatterns = [
    path('admin/', admin.site.urls),
    path('SingUp/', login, name="login"),
    path('logout/', logout, name="logout"),
    path('dashboard/', include('Dashboard.urls')),

    path('about/', about, name="about"),
    path('backlogs/', listar_backlogs, name="listar_backlogs"),
    path('suporte/', forms_support, name="forms_support"),

    path('api/', include('API.urls')),
    path('', include('social_django.urls', namespace='social')),
    path('callback/', callback, name='callback')
    
    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)