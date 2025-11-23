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
 
    path("credenciais/<str:username>/", views.CredenciaisUpsertView.as_view(), name="credenciais-upsert"),
    path("get-credenciais/<str:username>/", views.CredenciaisRetrieveView.as_view(), name="credenciais-get"),
    path("check-telefone/", views.CheckTelefoneView.as_view(), name="check_telefone"),
    path("telefone/<str:username>/", views.TelefoneView.as_view(), name="telefone-view"),
]
