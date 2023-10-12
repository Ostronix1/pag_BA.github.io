from django import forms
from .models import Asistencia  # Asegúrate de importar el modelo correcto
from .models import Voluntario

class VoluntarioForm(forms.ModelForm):
    class Meta:
        model = Voluntario
        fields = ['cedula', 'nombre', 'email', 'telefono']

#==============================================================================

class AsistenciaForm(forms.ModelForm):
    class Meta:
        model = Asistencia
        fields = ['cedula', 'nombre', 'fecha', 'horas', 'kg_derivados']
