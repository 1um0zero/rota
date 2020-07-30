from django import forms
from django.forms import ModelForm
from core.models import Curador

class CuradorForm(ModelForm):
    class Meta:
        model = Curador
        fields = '__all__'
        CATEGORIES = (
                ('', ''),
                ('curador', 'Curador(a)'),
                ('jurado', 'Jurado(a)'),
                )
        widgets = {
            'category': forms.Select(choices=CATEGORIES, attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['contest'].widget.attrs.update({'class': 'form-control'})
