from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('backlogs/listar/', views.listar_backlogs, name="listar_backlogs"),
    path('backlogs/criar/', views.forms_backlogs, name="forms_backlogs"),
    path('backlogs/editar/<int:pk>', views.editar_backlogs, name="editar_backlogs"),
    path('backlogs/remover/<int:pk>', views.remover_backlogs, name="remover_backlogs"),
]
