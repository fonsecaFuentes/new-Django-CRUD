from django import forms
from .models import Motor


class MotorForm(forms.ModelForm):
    class Meta:
        model = Motor
        fields = [
            'brand',
            'model',
            'hp',
            'rpm',
            'front_bearing',
            'rear_bearing',
            'anti_explosive',
            'description',
            'image'
        ]
        labels = {
            'brand': 'Marca',
            'model': 'Carcasa',
            'hp': 'HP',
            'rpm': 'RPM',
            'front_bearing': 'Rodamiento delantero',
            'rear_bearing': 'Rodamiento trasero',
            'anti_explosive': 'Antiexplosivo',
            'description': 'Descripción',
            'image': 'Imagen'
        }
