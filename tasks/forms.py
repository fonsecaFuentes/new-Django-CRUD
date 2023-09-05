from django import forms
from .models import Tasks


class TasksForm(forms.ModelForm):
    class Meta:
        model = Tasks
        fields = [
            'title',
            'description',
            'important',
            'completed',
            'image1',
            'image2'
        ]
        labels = {
            'title': 'Titulo',
            'description': 'Descripcion',
            'important': 'Es importante',
            'completed': 'Completado',
            'image1': 'Imagen',
            'image2': 'Imagen'
        }
