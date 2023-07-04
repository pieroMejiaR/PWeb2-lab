from django import forms
from .models import Destination

class DestinationForm(forms.ModelForm):
    class Meta:
        model = Destination
        fields = ['nombreCiudad', 'descripcionCiudad', 'imagenCiudad', 'precioTour', 'ofertaTour']
        widgets = {
            'descripcionCiudad': forms.Textarea(attrs={'rows': 3}),
        }
