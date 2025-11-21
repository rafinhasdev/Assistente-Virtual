from django.contrib import admin
from .models import Backlogs, SupportMensagens, SupportReplyMensagens

@admin.register(Backlogs)
class BacklogsAdmin(admin.ModelAdmin):
    list_display = ("num_versao", "data_postagem", "data_alteracao", "dev_responsavel")
    search_fields = ("num_versao", "dev_responsavel")
    list_filter = ("dev_responsavel",)
    date_hierarchy = "data_postagem"

@admin.register(SupportMensagens)
class SupportMensagensAdmin(admin.ModelAdmin):
    list_display = ("usuario", "data_envio", "ativo")
    search_fields = ("usuario__username",)
    list_filter = ("ativo",)
    date_hierarchy = "data_envio"

@admin.register(SupportReplyMensagens)
class SupportReplyMensagensAdmin(admin.ModelAdmin): 
    list_display = ("support", "data_envio", "dev_responsavel")
    search_fields = ("support__usuario__username",)
    list_filter = ("dev_responsavel",)
    date_hierarchy = "data_envio"



# Register your models here.
