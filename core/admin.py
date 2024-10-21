from django.contrib import admin
from core.models import Endereco, Trajeto, Treino, Corrida


class EnderecoAdmin(admin.ModelAdmin):
    list_display = ('rua', 'bairro', 'numero')
    search_fields = ('rua', 'bairro')

class TrajetoAdmin(admin.ModelAdmin):
    list_display = ('endereco_comeco', 'endereco_final', 'distancia', 'tempo_do_trajeto')
    search_fields = ('endereco_comeco',)

class TreinoAdmin(admin.ModelAdmin):
    list_display = ('trajeto', 'pace_realizado', 'data')
    search_fields = ('trajeto', 'data')

class CorridaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'distancia_realizada', 'posicao', 'trajeto', 'pace', 'data')
    search_fields = ('nome',)


admin.site.register(Endereco, EnderecoAdmin)
admin.site.register(Trajeto, TrajetoAdmin)
admin.site.register(Treino, TreinoAdmin)
admin.site.register(Corrida, CorridaAdmin)