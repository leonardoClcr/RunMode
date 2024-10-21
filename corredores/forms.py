from django import forms
from .models import Corredor  

class CorredorModelForm(forms.ModelForm):
    class Meta:
        model = Corredor
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(CorredorModelForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({'class': 'form-control'})
