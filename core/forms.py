from django import forms
from core.models import Endereco, Trajeto, Treino, Corrida


class CorridaModelForm(forms.ModelForm):
    class Meta:
        model = Corrida
        fields = '__all__'

class TreinoModelForm(forms.ModelForm):
    class Meta:
        model = Treino
        fields = '__all__'

class EnderecoModelForm(forms.ModelForm):
    class Meta:
        model = Endereco
        fields = '__all__'

    
class TrajetoModelForm(forms.ModelForm):
    class Meta:
        model = Trajeto
        fields = '__all__'