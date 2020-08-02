from django import forms

class AvaliacaoConcurso(forms.Form):
    estrutura_narrativa = forms.FloatField(label='Qualidade da Estrutura Narrativa', min_value=0)
    trama = forms.FloatField(label='Qualidade da Trama', min_value=0)
    personagens = forms.FloatField(label='Qualidade dos Personagens', min_value=0)
    dialogos = forms.FloatField(label='Qualidade dos Diálogos', min_value=0)
    originalidade = forms.FloatField(label='Originalidade*', min_value=0)
    
    protagonista_feminina = forms.ChoiceField(label='Tem protagonista feminina?', choices=[('sim', 'SIM'), ('nao', 'NÃO')], widget=forms.RadioSelect)
    premio_cabiria = forms.ChoiceField(label='Indicaria esta protagonista para o Prêmio Cabíria?', choices=[('sim', 'SIM'), ('nao', 'NÃO')], widget=forms.RadioSelect)
    nome_prot_feminina = forms.CharField(label='Caso afirmativo, qual o nome da personagem?', max_length=100, required=False,
                            widget=forms.TextInput(attrs={'class': 'avaliacao_texto'}))
    pesquisa = forms.CharField(label='PESQUISA ROTA: Qual o tema principal desenvolvido pelo roteiro?', max_length=300, required=False,
                            widget=forms.TextInput(attrs={'class': 'avaliacao_texto'}))

    indica_roteiro = forms.ChoiceField(label='Indica este roteiro para a categoria de melhor roteiro?', choices=[('sim', 'SIM'), ('nao', 'NÃO')], widget=forms.RadioSelect)
    indica_personagem = forms.ChoiceField(label='Indica este roteiro para a categoria de melhor personagem?', choices=[('sim', 'SIM'), ('nao', 'NÃO')], widget=forms.RadioSelect)
    indica_dialogo = forms.ChoiceField(label='Indica este roteiro para a categoria de melhor diálogo?', choices=[('sim', 'SIM'), ('nao', 'NÃO')], widget=forms.RadioSelect)
    
    def get_grades(self):
        return ['estrutura_narrativa','trama','personagens','dialogos','originalidade']
    
    def get_questions(self):
        return ['protagonista_feminina','premio_cabiria','nome_prot_feminina','pesquisa','indica_roteiro','indica_personagem','indica_dialogo']
    