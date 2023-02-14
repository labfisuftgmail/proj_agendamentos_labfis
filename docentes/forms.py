from django import forms
from .models import Curso, Docente

class CursoForm(forms.ModelForm):
    class Meta:
        model = Curso
        fields = "__all__"

    label = forms.CharField(
        widget = forms.HiddenInput(),
        initial = 'CursoForm'
    )

class DocenteForm(forms.ModelForm):
    STATUS_CHOICE = (
        ('Ativo', 'Ativo'),
        ('Inativo', 'Inativo'),
    )
    class Meta:
        model = Docente
        fields = "__all__"

    cursos = forms.ModelMultipleChoiceField(
        queryset = Curso.objects.all(),
        widget = forms.CheckboxSelectMultiple
    )

    status = forms.ChoiceField(
        widget = forms.RadioSelect,
        choices = STATUS_CHOICE
    )

    label = forms.CharField(
        widget = forms.HiddenInput(),
        initial = 'DocenteForm'
    )