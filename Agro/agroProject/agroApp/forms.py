from django import forms
from .models import RegistroActividad

class RegistroActividadForm(forms.ModelForm):
    class Meta:
        model = RegistroActividad
        fields = [
            'responsable',
            'actividad',
            'parcela'
        ]
        widgets = {
            'responsable': forms.TextInput(attrs={
                'placeholder': 'Nombre del responsable'
            }),
            'actividad': forms.Textarea(attrs={
                'placeholder': 'Describe el trabajo realizado',
                'rows': 5
            }),
            'parcela': forms.TextInput(attrs={
                'placeholder': 'Ej: Parcela 01'
            })
        }