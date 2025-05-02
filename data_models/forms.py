from django import forms
from .models import Brigada

class BrigadaForm(forms.ModelForm):
    class Meta:
        model = Brigada
        fields = ['nombre', 'direccion', 'curso', 'anio_escolar', 'caracterizacion', 'profesores']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre de la brigada'}),
            'direccion': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Dirección'}),
            'curso': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Curso'}),
            'anio_escolar': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Año escolar'}),
            'caracterizacion': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Caracterización'}),
            'profesores': forms.SelectMultiple(attrs={'class': 'form-control'}),
        }
        labels = {
            'nombre': 'Nombre',
            'direccion': 'Dirección',
            'curso': 'Curso',
            'anio_escolar': 'Año Escolar',
            'caracterizacion': 'Caracterización',
            'profesores': 'Profesores',
        }