from django.contrib import admin
from .models import Usuarios, Waha, Backlogs

admin.site.register(Usuarios)
admin.site.register(Backlogs)
admin.site.register(Waha)

# Register your models here.
