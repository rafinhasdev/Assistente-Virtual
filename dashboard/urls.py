from django.urls import path, include
from . import views 

urlpatterns = [
    path('', views.index, name="index"),
    path('support/', include('support.urls')),
    path('backlogs/', include('backlogs.urls')),
    path('usuarios/', include('usuarios.urls')),
]
