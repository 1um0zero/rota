from django import forms
from django.contrib.auth.models import User


class BillingForm(forms.Form):
    card_number = forms.CharField(max_length=20, required=True)
    card_holder = forms.CharField(max_length=100, required=True)
    card_date = forms.CharField(max_length=5, required=True)
    card_code = forms.CharField(max_length=4, required=True)
    cpf = forms.CharField(max_length=11, required=True)
    birthdate = forms.CharField(max_length=10, required=True)
    
    def clean(self):
        super().clean()
