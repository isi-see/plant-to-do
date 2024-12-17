from django import forms
from .models import Plant

class PlantForm(forms.ModelForm):
    class Meta:
        model = Plant
        fields = '__all__'

    # define custom widgets outside the Meta class for input of the date fields
    date_last_watered = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    date_last_fertilized = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    date_last_repotted = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
