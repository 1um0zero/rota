import os
from django import forms

class Lab(forms.Form):

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


    titulo = forms.CharField(max_length=100)

    genero = forms.CharField(max_length=100)

    logline = forms.CharField(max_length=100)

    numero_episodios = forms.IntegerField(min_value=0)

    tipo_formato = forms.MultipleChoiceField(
        widget=forms.CheckboxSelectMultiple,
        choices=[
            ('serializado', 'serializado'),
            ('procedural', 'procedural'),
            ('stand', 'stand alone'),
            ('arco aberto', 'arco aberto'),
            ('arco fechado', 'arco fechado'),
            ('multitrama', 'multitrama'),
            ('antologia', 'antologia'),
            ('minissérie', 'minissérie'),
            ('outro(s)', 'outro(s)'),
        ]
    )
    
    conceito = forms.CharField(max_length=2000, widget=forms.Textarea)

    arco_protagonista = forms.CharField(max_length=1000, widget=forms.Textarea, required=False)

    universo = forms.CharField(max_length=1500, widget=forms.Textarea)

    personagens = forms.CharField(max_length=2500, widget=forms.Textarea)

    arco_temporada = forms.CharField(max_length=3000, widget=forms.Textarea)

    temporadas_futuras = forms.CharField(max_length=2000, widget=forms.Textarea)

    sinopse = forms.FileField()

    responsibility = forms.FileField()

    rg = forms.CharField(max_length=20)
    rg_front = forms.FileField()
    rg_back = forms.FileField()

    curriculo = forms.FileField()

    registro_biblioteca = forms.FileField(required=False)

    documento_direitos = forms.FileField(required=False)

    letter = forms.FileField(required=False)
    letter2 = forms.FileField(required=False)

    def clean(self):
        super().clean()
        
        allowed_extensions = ['.png', '.jpg', '.jpeg', '.pdf']
        pic_fields = ['rg_front', 'rg_back', 'sinopse', 'responsibility',
            'curriculo', 'registro_biblioteca', 'documento_direitos', 'letter']

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

        print(self.errors)
        
