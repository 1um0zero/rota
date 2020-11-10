from django import forms
from django.forms import ModelForm
from core.models import Curador

class CuradorForm(ModelForm):
    class Meta:
        model = Curador
        fields = '__all__'
        CATEGORIES = (
                ('', ''),
                ('curador', 'Curador'),
                ('curadora', 'Curadora'),
                ('curador 2ª etapa', 'Curador 2ª etapa'),
                ('curadora 2ª etapa', 'Curadora 2ª etapa'),
                ('jurado', 'Jurado'),
                ('jurada', 'Jurada'),
                ('consultor', 'Consultor'),
                ('consultora', 'Consultora'),
                ('jurado de pitching', 'Jurado de Pitching'),
                ('jurada de pitching', 'Jurada de Pitching'),
                ('convidado', 'Convidado'),
                ('convidada', 'Convidada'),
                ('parceiro', 'Parceiro (Player)'),
                ('parceira', 'Parceira (Player)'),
                )
        widgets = {
            'category': forms.Select(choices=CATEGORIES, attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['contest'].widget.attrs.update({'class': 'form-control'})
