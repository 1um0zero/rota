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


class AvaliacaoConcursoJur(forms.Form):
    estrutura_narrativa = forms.FloatField(label='Qualidade da Estrutura Narrativa', min_value=0)
    trama = forms.FloatField(label='Qualidade da Trama', min_value=0)
    personagens = forms.FloatField(label='Qualidade dos Personagens', min_value=0)
    dialogos = forms.FloatField(label='Qualidade dos Diálogos', min_value=0)
    originalidade = forms.FloatField(label='Originalidade*', min_value=0)
    
    pesquisa = forms.CharField(label='PESQUISA ROTA: Qual o tema principal desenvolvido pelo roteiro?', max_length=300, required=False,
                            widget=forms.TextInput(attrs={'class': 'avaliacao_texto'}))

    indica_roteiro = forms.ChoiceField(label='Indica este roteiro para a categoria de melhor roteiro?', choices=[('sim', 'SIM'), ('nao', 'NÃO')], widget=forms.RadioSelect)
    indica_personagem = forms.ChoiceField(label='Indica este roteiro para a categoria de melhor personagem?', choices=[('sim', 'SIM'), ('nao', 'NÃO')], widget=forms.RadioSelect)
    indica_dialogo = forms.ChoiceField(label='Indica este roteiro para a categoria de melhor diálogo?', choices=[('sim', 'SIM'), ('nao', 'NÃO')], widget=forms.RadioSelect)
    
    def get_grades(self):
        return ['estrutura_narrativa','trama','personagens','dialogos','originalidade']
    
    def get_questions(self):
        return ['pesquisa','indica_roteiro','indica_personagem','indica_dialogo']


class AvaliacaoConcursoCabiria(forms.Form):
    indica_roteiro = forms.ChoiceField(label='Indica este roteiro para ser o vencedor do Prêmio Cabíria?', choices=[('sim', 'SIM'), ('nao', 'NÃO')], widget=forms.RadioSelect)
    def get_grades(self):
        return []
    
    def get_questions(self):
        return ['indica_roteiro']


class AvaliacaoLab(forms.Form):
    clareza = forms.FloatField(label='Clareza do Projeto', min_value=0)
    originalidade = forms.FloatField(label='Originalidade/Inventividade', min_value=0)
    universo = forms.FloatField(label='Domínio do universo', min_value=0)
    personagens = forms.FloatField(label='Construção dos personagens', min_value=0)
    atualidade = forms.FloatField(label='Relevância/atualidade*', min_value=0)
    
    indica_projeto = forms.ChoiceField(label='Aprovado para a próxima etapa? Recomendamos que a nota dos aprovados não seja inferior a 7,0', choices=[('sim', 'SIM'), ('nao', 'NÃO')], widget=forms.RadioSelect)
    
    def get_grades(self):
        return ['clareza', 'originalidade', 'universo', 'personagens', 'atualidade']
    
    def get_questions(self):
        return ['indica_projeto']


class AvaliacaoMostra(forms.Form):
    estrutura_narrativa = forms.FloatField(label='Qualidade da Estrutura Narrativa', min_value=0)
    trama = forms.FloatField(label='Qualidade da Trama', min_value=0)
    personagens = forms.FloatField(label='Qualidade dos Personagens', min_value=0)
    dialogos = forms.FloatField(label='Qualidade dos Diálogos', min_value=0)
    originalidade = forms.FloatField(label='Originalidade*', min_value=0)

    indica_curta = forms.ChoiceField(label='Seleciona este filme para a Mostra?', choices=[('sim', 'SIM'), ('nao', 'NÃO')], widget=forms.RadioSelect)    
    tematica_social = forms.ChoiceField(label='Tem temática social relevante?', choices=[('sim', 'SIM'), ('nao', 'NÃO')], widget=forms.RadioSelect)
    premio_sina = forms.ChoiceField(label='Indicaria para o Prêmio REDE SINA de Temática Social?', choices=[('sim', 'SIM'), ('nao', 'NÃO')], widget=forms.RadioSelect)    
    pesquisa = forms.CharField(label='PESQUISA ROTA: Qual o tema principal desenvolvido pelo roteiro?', max_length=300, required=False,
                            widget=forms.TextInput(attrs={'class': 'avaliacao_texto'}))
            
    def get_grades(self):
        return ['estrutura_narrativa','trama','personagens','dialogos','originalidade']
    
    def get_questions(self):
        return ['indica_curta', 'tematica_social', 'premio_sina', 'pesquisa']
    

class AvaliacaoMostraJur(forms.Form):
    indica_ficcao = forms.ChoiceField(label='Indica este filme para a categoria de Melhor Ficção?', choices=[('sim', 'SIM'), ('nao', 'NÃO')], widget=forms.RadioSelect)
    indica_doc = forms.ChoiceField(label='Indica este filme para a categoria de Melhor Documentário?', choices=[('sim', 'SIM'), ('nao', 'NÃO')], widget=forms.RadioSelect)
    def get_grades(self):
        return []
    
    def get_questions(self):
        return ['indica_ficcao', 'indica_doc']

class AvaliacaoMostraSina(forms.Form):
    indica_curta = forms.ChoiceField(label='Indica este filme para ser o vencedor do Prêmio Rede Sina?', choices=[('sim', 'SIM'), ('nao', 'NÃO')], widget=forms.RadioSelect)
    def get_grades(self):
        return []
    
    def get_questions(self):
        return ['indica_curta']