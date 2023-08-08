from django import forms
from .models import Coupling


class CouplingForm(forms.ModelForm):
    class Meta:
        model = Coupling
        fields = '__all__'
