from corredores.models import Corredor
from django.views.generic import ListView, CreateView, DeleteView, DetailView
from corredores.forms import CorredorModelForm


class CorredorListView(ListView):
    model = Corredor
    template_name = 'corredor_list.html'
    context_object_name = 'corredores'


class CorredorCreateView(CreateView):
    model = Corredor
    form_class = CorredorModelForm
    template_name = 'novo_corredor.html'
    success_url = '/corredores/'


class CorredorDeleteView(DeleteView):
    model = Corredor
    template_name = 'deletar_corredor.html'
    success_url = '/corredores/'


class CorredorDetailView(DetailView):
    model = Corredor
    template_name = 'detalhes_corredor.html'
    context_object_name = 'corredores'