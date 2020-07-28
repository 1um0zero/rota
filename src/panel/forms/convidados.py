from django import forms
from django.forms import ModelForm
from core.models import Curador

class CuradorForm(ModelForm):
    class Meta:
        model = Curador
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['contest'].widget.attrs.update({'class': 'form-control'})
"""
    contests = Contest.objects.all()

    name = forms.CharField()
    contest_id = forms.ChoiceField(
        required=False,
        choices=([('', '')] +
            [(contest.id, contest.name) for contest in Contest.objects.all()]),
        widget=forms.Select(attrs={'class':'form-control'})
    )
    bio = forms.CharField(required=False)
    picture = forms.FileField(required=False)
"""