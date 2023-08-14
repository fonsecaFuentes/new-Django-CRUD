from django import forms
from .models import Coupling


class CouplingForm(forms.ModelForm):

    class Meta:
        model = Coupling
        fields = [
            'types',
            'model',
            'motor_side_measure',
            'pump_side_sizer',
            'motor_key_measure',
            'pump_key_measure',
            'description',
            'image'
        ]
        labels = {
            'types': 'Tipo de acople',
            'model': 'Serie',
            'motor_side_measure': 'Medida eje lado motor',
            'pump_side_sizer': 'Medida eje lado bomba',
            'motor_key_measure': 'Medida chaveta lado motor',
            'pump_key_measure': 'Medida chaveta lado bomba',
            'description': 'Descripción',
            'image': 'Imagen'
        }
