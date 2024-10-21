from django import forms
from core.models import Endereco, Trajeto

class EnderecoModelForm(forms.ModelForm):
    class Meta:
        model = Endereco
        fields = '__all__'

    
class TrajetoModelForm(forms.ModelForm):
    class Meta:
        model = Trajeto
        fields = '__all__'