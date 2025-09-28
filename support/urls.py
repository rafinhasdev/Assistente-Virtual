from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('support/', views.support, name='support'),
    path('support_listar/', views.support_listar, name='support_listar'),
    path('support_criar/', views.support_criar, name='support_criar'),
    path('support_remover/<int:pk>/', views.support_remover, name='support_remover'),
]
    