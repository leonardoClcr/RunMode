from django.views.generic import ListView, CreateView, DeleteView, UpdateView
from core.forms import EnderecoModelForm
from core.models import Endereco, Trajeto


class TrajetoListView(ListView):
    model = Trajeto
    template_name = 'lista_trajeto.html'
    context_object_name = 'trajetos'
    

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