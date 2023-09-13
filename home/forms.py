from django import forms
from .models import İhaUyeModel

class IhaUyeForm(forms.ModelForm):
    class Meta:
        model = İhaUyeModel  # İlgili modeli belirtin
        fields = ['ihalar', 'uye']  # Düzenlenecek alanları belirtin
