from django import forms
from .models import Estrategia, Evento, Profesor, Reporte, RegistroUsuario, Encuesta

# Formulario para el modelo Estrategia
class EstrategiaForm(forms.ModelForm):
    class Meta:
        model = Estrategia
        fields = '__all__'

# Formulario para el modelo Evento
class EventoForm(forms.ModelForm):
    class Meta:
        model = Evento
        fields = '__all__'

# Formulario para el modelo Profesor
class ProfesorForm(forms.ModelForm):
    class Meta:
        model = Profesor
        fields = '__all__'

# Formulario para el modelo Reporte
class ReporteForm(forms.ModelForm):
    class Meta:
        model = Reporte
        fields = '__all__'

# Formulario para el modelo RegistroUsuario
class RegistroUsuarioForm(forms.ModelForm):
    class Meta:
        model = RegistroUsuario
        fields = '__all__'

# Formulario para el modelo Encuesta
class EncuestaForm(forms.ModelForm):
    class Meta:
        model = Encuesta
        fields = '__all__'
