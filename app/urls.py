from django.contrib import admin
from django.urls import path
from corredores.views import CorredorListView, CorredorCreateView, CorredorDeleteView, CorredorDetailView
from core.views import EnderecoCreateView, EnderecoListView, EnderecoDeleteView, EnderecoUpdateView, TrajetoListView, TrajetoCreateView, TrajetoDeleteView, TrajetoUpdateView, TreinoListView, TreinoCreateView, TreinoDeleteView, TreinoUpdateView, CorridaListView, CorridaDeleteView, CorridaCreateView, CorridaUpdateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('corredores/', CorredorListView.as_view(), name='corredores'),
    path('corredores/<int:pk>/deletar', CorredorDeleteView.as_view(), name='corredor_deletar'),
    path('corredores/<int:pk>/', CorredorDetailView.as_view(), name='corredor_detalhes'),
    path('novo_corredor/', CorredorCreateView.as_view(), name='novo_corredor'),

    path('novo_endereco/', EnderecoCreateView.as_view(), name='novo_endereco'),
    path('enderecos/', EnderecoListView.as_view(), name='enderecos'),
    path('enderecos/<int:pk>/deletar', EnderecoDeleteView.as_view(), name='endereco_deletar'),
    path('enderecos/<int:pk>/atualizar', EnderecoUpdateView.as_view(), name='endereco_atualizar'),

    path('lista_trajetos/', TrajetoListView.as_view(), name='trajetos'),
    path('novo_trajeto/', TrajetoCreateView.as_view(), name='novo_trajeto'),
    path('lista_trajetos/<int:pk>/deletar', TrajetoDeleteView.as_view(), name='deletar_trajeto'),
    path('lista_trajetos/<int:pk>/atualizar', TrajetoUpdateView.as_view(), name='atualizar_trajeto'),

    path('treinos/', TreinoListView.as_view(), name='treinos'),
    path('criar_treinos/', TreinoCreateView.as_view(), name='criar_treino'),
    path('treinos/<int:pk>/deletar', TreinoDeleteView.as_view(), name='deletar_treino'),
    path('treinos/<int:pk>/atualizar', TreinoUpdateView.as_view(), name='atualizar_treino'),

    
    path('corridas/', CorridaListView.as_view(), name='corridas'),
    path('criar_corridas/', CorridaCreateView.as_view(), name='criar_corrida'),
    path('corridas/<int:pk>/deletar', CorridaDeleteView.as_view(), name='deletar_corrida'),
    path('corridas/<int:pk>/atualizar', CorridaUpdateView.as_view(), name='atualizar_corrida'),
]   
