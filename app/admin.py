from django.contrib import admin
from .models import Usuarios, Waha, Backlogs, Credenciais, SupportMensagens

admin.site.register(Usuarios)
admin.site.register(Backlogs)
admin.site.register(Waha)
admin.site.register(Credenciais)
admin.site.register(SupportMensagens)

# Register your models here.
