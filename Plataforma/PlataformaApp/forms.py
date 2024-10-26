from django import forms
from PlataformaApp.models import Plataforma

class FormPlataforma(forms.ModelForm):
    class Meta:
        model = Plataforma
        fields = '__all__'
        widgets = {
            'tipo': forms.Select(attrs={'placeholder': 'Seleccione el tipo'}),
            'generacion': forms.TextInput(attrs={'placeholder': 'Ingrese la generación'}),
            'almacenamiento': forms.NumberInput(attrs={'placeholder': 'Ingrese el almacenamiento en GB'}),
            'fabricante': forms.TextInput(attrs={'placeholder': 'Ingrese el fabricante'}),
            'precio': forms.NumberInput(attrs={'placeholder': 'Ingrese el precio'}),
        }
