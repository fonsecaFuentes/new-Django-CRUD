from django import forms
from .models import Pumps
from .models import Bearing
from .models import MechanicalSeal
from .models import Reten


class PumpsForm(forms.ModelForm):
    class Meta:
        model = Pumps
        fields = [
            'tag',
            'brand',
            'model',
            'types',
            'description',
            'image'
        ]
        labels = {
            'types': 'Tipo de Bomba',
            'brand': 'Marca',
            'model': 'Modelo',
            'tag': 'TAG',
            'description': 'Descripción',
            'image': 'Imagen de la Bomba',
        }


class BearingForm(forms.ModelForm):
    class Meta:
        model = Bearing
        fields = [
            'types',
            'amount',
            'front_bearing',
            'rear_bearing',
            'description',
        ]
        labels = {
            'types': 'Tipo de Rodamientos',
            'amount': 'Cantidad',
            'front_bearing': 'Rodamientos delanteros',
            'rear_bearing': 'Rodamientos traseros',
            'description': 'Descripción',
        }


class MechanicalSealForm(forms.ModelForm):
    class Meta:
        model = MechanicalSeal
        fields = [
            'extention',
            'brand',
            'types',
            'description',
        ]
        labels = {
            'extention': 'Medida',
            'types': 'Tipo de Sello',
            'brand': 'Marca',
            'description': 'Descripción',
        }


class RetenForm(forms.ModelForm):
    class Meta:
        model = Reten
        fields = [
            'front_seal',
            'rear_seal',
            'details',
        ]
        labels = {
            'front_seal': 'Número de serie Reten delantero',
            'rear_seal': 'Número de serie Reten trasero',
            'details': 'Descripción',
        }
