from django.contrib import admin
from .models import Usuarios

@admin.register(Usuarios)
class UsuariosAdmin(admin.ModelAdmin):
    list_display = ("username", "email", "numero", "first_name", "last_name")
    search_fields = ("username", "email", "first_name", "last_name")
    date_hierarchy = "date_joined"

# Register your models here.
