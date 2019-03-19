from django import forms
from contact.models import Contato

class CriarContatoForm(forms.ModelForm):
    class Meta: 
        model: Contato
        fields: [
            'nome',
            'sobrenome', 
            'email',
            'telefone',
            'celular', 
        ]
