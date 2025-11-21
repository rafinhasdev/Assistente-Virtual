from django.urls import path

from API import views

urlpatterns = [
    path(
        "cadastrar/",
        views.CredenciaisCreateView.as_view(),
        name="cadastrar-credenciais",
    ),
    path("usuarios/", views.UsuariosListView.as_view(), name="listar-usuarios"),
    path(
        "usuarios/<int:pk>/delete/",
        views.UsuariosDeleteView.as_view(),
        name="deletar-usuario",
    ),
    path(
        "usuarios-slim/",
        views.UsuariosSlimListView.as_view(),
        name="listar-usuarios-slim",
    ),
    path(
        "getcredentiais/", views.CredenciaisListView.as_view(), name="get_credentiais"
    ),
    path("check-telefone/", views.CheckTelefoneView.as_view(), name="check_telefone"),
    path(
        "usuarios/<str:matricula>/update-telefone/",
        views.UpdateTelefonePorMatriculaView.as_view(),
        name="update_telefone",
    ),
]
