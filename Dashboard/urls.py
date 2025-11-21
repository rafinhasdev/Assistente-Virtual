from django.urls import path

from .views import *

urlpatterns = [
    path("", index, name="dashboard_index"),
    path("backlogs/", BacklogsListView.as_view(), name="backlogs_list"),
    path("backlogs/<int:pk>/", BacklogsDetailView.as_view(), name="backlogs_detail"),
    path("backlogs/create/", BacklogsCreateView.as_view(), name="backlogs_create"),
    path(
        "backlogs/<int:pk>/update/",
        BacklogsUpdateView.as_view(),
        name="backlogs_update",
    ),
    path(
        "backlogs/delete/<int:pk>/",
        BacklogsDeleteView.as_view(),
        name="backlogs_delete",
    ),
    path("support/", SupportMensagensListView.as_view(), name="support_list"),
    path(
        "support/<int:pk>/", SupportMensagensDetailView.as_view(), name="support_detail"
    ),
    path(
        "support/create/", SupportMensagensCreateView.as_view(), name="support_create"
    ),
    path(
        "support/<int:pk>/update/",
        SupportMensagensUpdateView.as_view(),
        name="support_update",
    ),
    path(
        "support/delete/<int:pk>/",
        SupportMensagensDeleteView.as_view(),
        name="support_delete",
    ),
    path("usuarios/", UsuariosListView.as_view(), name="usuarios_list"),
    path("usuarios/<int:pk>/", UsuariosDetailView.as_view(), name="usuarios_detail"),
    path(
        "usuarios/<int:pk>/update/",
        UsuariosUpdateView.as_view(),
        name="usuarios_update",
    ),
    path(
        "usuarios/<int:pk>/delete/",
        UsuariosDeleteView.as_view(),
        name="usuarios_delete",
    ),
    path(
    "support/<int:pk>/reply/",
    SupportMensagemReplyView.as_view(),
    name="support_reply",
    ),
]
