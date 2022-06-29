from django import forms
from .models import InformationModel


class InformationForm(forms.ModelForm):
    class Meta:
        model = InformationModel
        fields = ['destination']
