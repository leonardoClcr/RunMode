from django.contrib import admin
from django.urls import path
from corredores.views import CorredorListView, CorredorCreateView, CorredorDeleteView, CorredorDetailView
from core.views import EnderecoCreateView, EnderecoListView, EnderecoDeleteView, EnderecoUpdateView, TrajetoListView

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

    path('lista_trajetos', TrajetoListView.as_view(), name='trajetos')
]   
