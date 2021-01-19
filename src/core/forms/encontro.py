import os
from django import forms

class Encontro(forms.Form):

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

    pfpj = forms.ChoiceField(widget=forms.RadioSelect, choices=[
        ('pf', 'Pessoa física'), ('pj', 'Pessoa jurídica')
    ])

    rg = forms.CharField(max_length=20, required=False)
    # rg_front = forms.FileField()
    # rg_back = forms.FileField()

    cnpj = forms.CharField(max_length=20, required=False)
    razao_social = forms.CharField(max_length=20, required=False)
    nome_fantasia = forms.CharField(max_length=20, required=False)

    titulo = forms.CharField(max_length=100)

    registro_biblioteca = forms.FileField()

    caracteristicas_1 = forms.ChoiceField(
        widget=forms.RadioSelect,
        choices=[(gen, gen) for gen in [
            'ficção', 'não ficção', 'outro',
        ]]
    )
    
    caracteristicas_2 = forms.ChoiceField(
        widget=forms.RadioSelect,
        choices=[(gen, gen) for gen in [
            'sim', 'não',
        ]]
    )

    caracteristicas_3 = forms.ChoiceField(
        widget=forms.RadioSelect,
        choices=[(gen, gen) for gen in [
            'curta', 'média', 'longa',
        ]]
    )

    # caracteristicas_4 = forms.CharField(max_length=100)
    
    #veiculo = forms.MultipleChoiceField(
    #    widget=forms.CheckboxSelectMultiple,
    #    choices=[(gen, gen) for gen in [
    #        'Celular', 'Cinema', 'Streaming', 'TV', 'Outros',
    #    ]]
    #)
    

    genero = forms.MultipleChoiceField(
        widget=forms.CheckboxSelectMultiple,
        choices=[(gen, gen) for gen in ['Ação', 'Aventura', 'Biográfico', 'Comédia', 'Drama',
            'Dramédia', 'Fantasia', 'Híbrido', 'Histórico', 'Infantil', 'Sci-fi', 'Suspense', 'Terror', 'Outros']
            ]
    )

    logline = forms.CharField(max_length=2048)

    sinopse = forms.FileField()

    argumento = forms.FileField()

    personagens = forms.CharField(max_length=2500, widget=forms.Textarea)

    publico_alvo = forms.CharField(max_length=1000, widget=forms.Textarea)

    biografia = forms.CharField(max_length=500, widget=forms.Textarea)

    info_adicional = forms.CharField(max_length=500, widget=forms.Textarea)

    #parceiro = forms.FileField(required=False)


    def clean(self):
        super().clean()
        
        allowed_extensions = ['.png', '.jpg', '.jpeg', '.pdf']
        pic_fields = ['rg_front', 'rg_back', 'registro_biblioteca']

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

        if 'pfpj' in self.cleaned_data:

            if self.cleaned_data['pfpj'] == 'pf':
                if self.cleaned_data['rg'] == '':
                    self.add_error('rg', 'Informe o RG.')

            elif self.cleaned_data['pfpj'] == 'pj':
                if self.cleaned_data['cnpj'] == '':
                    self.add_error('cnpj', 'Informe o CNPJ.')

        print(self.errors)
        
