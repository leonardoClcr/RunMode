from django.contrib import admin
from corredores.models import Corredor

class CorredorAdmin(admin.ModelAdmin):
    list_display = ('nome', 'idade', 'peso', 'altura')

admin.site.register(Corredor, CorredorAdmin)