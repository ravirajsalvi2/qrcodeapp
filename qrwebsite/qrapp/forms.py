from django import forms
from .models import QRCode

class QRCodeForm(forms.ModelForm):
    class Meta:
        model = QRCode
        fields = ['data', 'overlay_image']  # Includes the uploaded image
        widgets = {
            'data': forms.Textarea(attrs={'rows': 4, 'cols': 40}),
        }

