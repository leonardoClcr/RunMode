from django.views.generic import ListView, CreateView, DeleteView, UpdateView
from core.forms import EnderecoModelForm, TrajetoModelForm
from core.models import Endereco, Trajeto


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