from django.views.generic import ListView, CreateView, DeleteView, UpdateView
from core.forms import EnderecoModelForm, TrajetoModelForm, TreinoModelForm, CorridaModelForm
from core.models import Endereco, Trajeto, Treino, Corrida


class CorridaListView(ListView):
    model = Corrida
    template_name = 'lista_corrida.html'
    context_object_name = 'corridas'


class CorridaCreateView(CreateView):
    model = Corrida
    form_class = CorridaModelForm
    template_name = 'criar_corrida.html'
    success_url = '/corridas/'


class CorridaDeleteView(DeleteView):
    model = Corrida
    template_name = 'deletar_corrida.html'
    success_url = '/corridas/'


class CorridaUpdateView(UpdateView):
    model = Corrida
    form_class = CorridaModelForm
    template_name = 'atualizar_corrida.html'
    success_url = '/corridas/'


class TreinoListView(ListView):
    model = Treino
    template_name = 'lista_treino.html'
    context_object_name = 'treinos'


class TreinoCreateView(CreateView):
    model = Treino
    form_class = TreinoModelForm
    template_name = 'criar_treino.html'
    success_url = '/treinos/'


class TreinoDeleteView(DeleteView):
    model = Treino
    template_name = 'deletar_treino.html'
    success_url = '/treinos/'


class TreinoUpdateView(UpdateView):
    model = Treino
    form_class = TrajetoModelForm
    template_name = 'atualizar_treino.html'
    success_url = '/treinos/'


class TrajetoListView(ListView):
    model = Trajeto
    template_name = 'lista_trajeto.html'
    context_object_name = 'trajetos'
    

class TrajetoCreateView(CreateView):
    model = Trajeto
    form_class = TrajetoModelForm
    template_name = 'criar_trajeto.html'
    success_url = '/lista_trajetos/'


class TrajetoDeleteView(DeleteView):
    model = Trajeto
    template_name = 'deletar_trajeto.html'
    success_url = '/lista_trajetos/'


class TrajetoUpdateView(UpdateView):
    model = Trajeto
    form_class = TrajetoModelForm
    template_name = 'atualizar_trajeto.html'
    success_url = '/lista_trajetos/'


class EnderecoCreateView(CreateView):
    model = Endereco
    form_class = EnderecoModelForm
    template_name = 'criar_endereco.html'
    success_url = '/enderecos/'


class EnderecoListView(ListView):
    model = Endereco
    template_name = 'lista_endereco.html'
    context_object_name = 'enderecos'
    

class EnderecoDeleteView(DeleteView):
    model = Endereco
    template_name = 'deletar_endereco.html'
    success_url = '/enderecos/'


class EnderecoUpdateView(UpdateView):
    model = Endereco
    form_class = EnderecoModelForm
    template_name = 'atualizar_endereco.html'
    success_url = '/enderecos/'