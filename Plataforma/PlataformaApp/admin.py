from django.contrib import admin
from PlataformaApp.models import Plataforma


class PlataformaAdmin(admin.ModelAdmin):
    list_display = ['tipo', 'generacion', 'almacenamiento', 'fabricante', 'precio']


# Register your models here.
admin.site.register(Plataforma, PlataformaAdmin)