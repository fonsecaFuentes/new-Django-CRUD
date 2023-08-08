from django import forms
from .models import Motor


class MotorForm(forms.ModelForm):
    class Meta:
        model = Motor
        fields = '__all__'
