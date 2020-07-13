import re
from django import forms
from django.contrib.auth.models import User


class SignupForm(forms.Form):
    name = forms.CharField(label='Nome completo', max_length=100)
    email = forms.EmailField(max_length=150, required=True, error_messages={
        'invalid': 'Digite um email válido.'
    })
    ddd = forms.CharField(label='DDD', max_length=2)
    phone = forms.CharField(label='Telefone celular com DDD', max_length=30)
    pass1 = forms.CharField(label='Senha', max_length=30,
        widget=forms.PasswordInput())
    pass2 = forms.CharField(label='Confirmar senha', max_length=30,
        widget=forms.PasswordInput(), required=True)
    
    def clean(self):
        super().clean()
        
        if 'email' in self.cleaned_data:
            email_exists = User.objects.filter(
                username=self.cleaned_data['email'])
            if email_exists:
                self.add_error('email', 'Esse email já está cadastrado.')
        
        if not re.findall('^([0-9]{2})$', self.cleaned_data['ddd']):
            self.add_error('ddd', 'Digite o DDD.')

        if not re.findall('^([0-9]{5})\-([0-9]{4})$', self.cleaned_data['phone']):
            self.add_error('phone', 'Digite um telefone válido.')

        if self.cleaned_data['pass1'] != self.cleaned_data['pass2']:
            self.add_error('pass1', 'As senhas digitadas não são iguais.')
