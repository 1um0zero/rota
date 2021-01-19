import os
from django import forms

class ConcursoRoteiros(forms.Form):
    title = forms.CharField(max_length=200)

    nickname = forms.CharField(max_length=200)

    rg = forms.CharField(max_length=20)
    rg_front = forms.FileField()
    rg_back = forms.FileField()

    cep = forms.CharField(max_length=9)
    address = forms.CharField(max_length=200)
    address_number = forms.CharField(max_length=10)
    address_complement = forms.CharField(max_length=100, required=False)
    address_neighborhood = forms.CharField(max_length=100)
    address_city = forms.CharField(max_length=100)
    address_state = forms.ChoiceField(choices=[
        ('', ''),
        ('RJ', 'Rio de Janeiro'),
        ('AC', 'Acre'),
        ('AL', 'Alagoas'),
        ('AP', 'Amapá'),
        ('AM', 'Amazonas'),
        ('BA', 'Bahia'),
        ('CE', 'Ceará'),
        ('DF', 'Distrito Federal'),
        ('ES', 'Espírito Santo'),
        ('GO', 'Goiás'),
        ('MA', 'Maranhão'),
        ('MT', 'Mato Grosso'),
        ('MS', 'Mato Grosso do Sul'),
        ('MG', 'Minas Gerais'),
        ('PA', 'Pará'),
        ('PB', 'Paraíba'),
        ('PR', 'Paraná'),
        ('PE', 'Pernambuco'),
        ('PI', 'Piauí'),
        ('RJ', 'Rio de Janeiro'),
        ('RN', 'Rio Grande do Norte'),
        ('RS', 'Rio Grande do Sul'),
        ('RO', 'Rondônia'),
        ('RR', 'Roraima'),
        ('SC', 'Santa Catarina'),
        ('SP', 'São Paulo'),
        ('SE', 'Sergipe'),
        ('TO', 'Tocantins'),
    ])

    phone_home_ddd = forms.CharField(max_length=200, required=False)
    phone_home = forms.CharField(max_length=200, required=False)

    max_subscriptions = forms.ChoiceField(choices=[('sim', 'SIM'), ('nao', 'NÃO')],
        widget=forms.RadioSelect)

    max_pages = forms.ChoiceField(choices=[('sim', 'SIM'), ('nao', 'NÃO')],
        widget=forms.RadioSelect)

    coauthors = forms.ChoiceField(choices=[('sim', 'SIM'), ('nao', 'NÃO')],
        widget=forms.RadioSelect)

    is_original = forms.ChoiceField(choices=[('original', 'ORIGINAL'), ('adaptado', 'ADAPTADO')],
        widget=forms.RadioSelect)

    authorize = forms.ChoiceField(choices=[('sim', 'SIM'), ('nao', 'NÃO')],
        widget=forms.RadioSelect)

    is_student = forms.ChoiceField(choices=[('iniciante', 'INICIANTE'), ('estudante', 'ESTUDANTE')],
        widget=forms.RadioSelect)

    longa_filmado = forms.ChoiceField(choices=[('sim', 'SIM'), ('nao', 'NÃO')],
        widget=forms.RadioSelect)

    serie_filmado = forms.ChoiceField(choices=[('sim', 'SIM'), ('nao', 'NÃO')],
        widget=forms.RadioSelect)
    
    curta_mais_tres = forms.ChoiceField(choices=[('sim', 'SIM'), ('nao', 'NÃO')],
        widget=forms.RadioSelect)

    script = forms.FileField()

    responsibility = forms.FileField()

    documento_direitos = forms.FileField(required=False)

    letter = forms.FileField(required=False)
    letter2 = forms.FileField(required=False)


    def clean(self):
        super().clean()
        
        if 'max_subscriptions' in self.cleaned_data \
                and self.cleaned_data['max_subscriptions'] == 'nao':
            self.add_error('max_subscriptions', 'Você só pode enviar até 03 (três) roteiros.')

        if 'max_pages' in self.cleaned_data \
                and self.cleaned_data['max_pages'] == 'nao':
            self.add_error('max_pages', 'Formato inválido.')

        if 'longa_filmado' in self.cleaned_data \
                and self.cleaned_data['longa_filmado'] == 'sim':
            self.add_error('longa_filmado', 'Você não pode ter um longa filmado!')

        if 'serie_filmado' in self.cleaned_data \
                and self.cleaned_data['serie_filmado'] == 'sim':
            self.add_error('serie_filmado', 'Você não pode ter um episódio de série filmado!')
        
        if 'curta_mais_tres' in self.cleaned_data \
                and self.cleaned_data['curta_mais_tres'] == 'sim':
            self.add_error('curta_mais_tres', 'Você não pode ter mais que três roteiros de curta filmados!')
        
        # if 'authorize' in self.cleaned_data \
                # and self.cleaned_data['authorize'] == 'nao':
            # self.add_error('authorize', 'Você precisa autorizar a inclusão do roteiro.')

        allowed_extensions = ['.png', '.jpg', '.jpeg', '.pdf']
        pic_fields = ['rg_front', 'rg_back', 'script', 'responsibility', 'letter']

        for filefield in pic_fields:
            if filefield in self.cleaned_data and self.cleaned_data[filefield]:

                filename = self.cleaned_data[filefield].name
                ext = os.path.splitext(filename)[1].lower()

                if ext not in allowed_extensions:

                    errorfield = filefield

                    if errorfield in ['rg_front', 'rg_back']:
                        errorfield = 'rg'

                    self.add_error(errorfield,
                        ('Tipo de arquivo inválido. Formatos permitidos: '
                            'PDF, JPG, PNG.'))

        
