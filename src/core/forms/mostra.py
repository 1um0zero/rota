import os
import re
from django import forms

class MostraCompetitiva(forms.Form):


    titulo = forms.CharField(max_length=200)
    url = forms.CharField(max_length=255)
    #url_pass = forms.CharField(max_length=255, required=False)
    sinopse = forms.CharField(widget=forms.Textarea)

    duracao = forms.CharField(max_length=30)
    ano = forms.IntegerField(min_value=1900)
    cidade = forms.CharField(max_length=50)
    estado = forms.ChoiceField(choices=[
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
    categoria = forms.ChoiceField(choices=[(1, 'Ficção'), (2, 'Documentário')],
        widget=forms.RadioSelect)

    classificacao = forms.ChoiceField(choices=[
        (1, 'Livre'), (2, '10 anos'), (3, '12 anos'), (4, '14 anos'),
        (5, '16 anos'), (6, '18 anos')
    ], widget=forms.RadioSelect)

    formato_finalizacao = forms.CharField(max_length=100)
    formato_exibicao = forms.CharField(max_length=100)
    formato_janela = forms.CharField(max_length=100)
    som = forms.CharField(max_length=30)
    cor = forms.ChoiceField(choices=[(1, 'PB'), (2, 'Cor')], widget=forms.RadioSelect)
    cpb = forms.CharField(max_length=30)
    site = forms.CharField(max_length=255, required=False)
    facebook = forms.CharField(max_length=255, required=False)
    festivais = forms.CharField(widget=forms.Textarea)
    premios = forms.CharField(widget=forms.Textarea)
    foto_1 = forms.FileField()
    foto_2 = forms.FileField(required=False)
    foto_3 = forms.FileField(required=False)

    roteirista = forms.CharField(max_length=100)
    #diretor = forms.CharField(max_length=100)
    #diretor_producao = forms.CharField(max_length=100)
    #produtor_executivo = forms.CharField(max_length=100)
    #fotografia = forms.CharField(max_length=100)
    #trilha = forms.CharField(max_length=100)
    #montagem = forms.CharField(max_length=100)
    #direcao_arte = forms.CharField(max_length=100)
    #tec_som = forms.CharField(max_length=100)
    #edicao_som = forms.CharField(max_length=100)
    #elenco = forms.CharField(widget=forms.Textarea)

    rg = forms.CharField(max_length=20)
    rg_front = forms.FileField()
    rg_back = forms.FileField()

    nascimento = forms.CharField(max_length=100)
    phone_home_ddd = forms.CharField(max_length=200)
    phone_home = forms.CharField(max_length=200)

    cep = forms.CharField(max_length=9)
    address = forms.CharField(max_length=200)
    address_number = forms.CharField(max_length=10)
    address_complement = forms.CharField(max_length=100)
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


    max_filmes = forms.ChoiceField(choices=[('sim', 'SIM'), ('nao', 'NÃO')], 
        widget=forms.RadioSelect)
    
    max_min = forms.ChoiceField(choices=[('sim', 'SIM'), ('nao', 'NÃO')],
        widget=forms.RadioSelect)

    is_student = forms.ChoiceField(choices=[('iniciante', 'INICIANTE'), ('estudante', 'ESTUDANTE')],
        widget=forms.RadioSelect)

    responsibility = forms.FileField()

    letter1 = forms.FileField(required=False)

    letter2 = forms.FileField(required=False)

    def clean(self):
        super().clean()

        if 'max_filmes' in self.cleaned_data \
                and self.cleaned_data['max_filmes'] == 'nao':
            self.add_error('max_filmes', 'Você só pode inscrever até 03 (três) filmes.')

        if 'max_min' in self.cleaned_data \
                and self.cleaned_data['max_min'] == 'nao':
            self.add_error('max_min', 'O filme deve ter até 20 minutos incluindo os créditos.')

        if 'url' in self.cleaned_data \
                and not re.findall('^https?://', self.cleaned_data['url']):
            self.add_error('url', 'URL inválida.')

        if 'site' in self.cleaned_data and self.cleaned_data['site'] \
                and not re.findall('^https?://', self.cleaned_data['site']):
            self.add_error('site', 'URL inválida.')

        if 'facebook' in self.cleaned_data and self.cleaned_data['facebook'] \
                and not re.findall('^https?://', self.cleaned_data['facebook']):
            self.add_error('facebook', 'URL inválida.')

        allowed_extensions = ['.png', '.jpg', '.jpeg', '.pdf']
        pic_fields = ['responsibility']

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

