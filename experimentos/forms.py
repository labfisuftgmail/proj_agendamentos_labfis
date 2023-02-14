from django import forms
from .models import Area, Arquivo, Experimento

class ArquivoForm(forms.ModelForm):
    class Meta:
        model = Arquivo
        fields = "__all__"