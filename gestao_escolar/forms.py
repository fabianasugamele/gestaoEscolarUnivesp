from django import forms
from .models import AnexoAluno

class AnexoForm(forms.ModelForm):
    class Meta:
        model = AnexoAluno
        fields = ['tipo_documento']