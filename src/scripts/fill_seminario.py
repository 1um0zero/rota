from core.models import Seminario
import datetime
import pytz
from django.utils.timezone import make_aware

def run(*args):
    try:
        
        dados = [
            {'name': 'A relação entre roteiro audiovisual e dramaturgia', 'date': datetime.datetime(2021, 3, 16, 19, 0, tzinfo=pytz.UTC), 'description': 'Maria Shu e Renata Mizrahi'},
            {'name': 'Mesa de Debates: Pesquisa em roteiro no Brasil', 'date': datetime.datetime(2021, 3, 16, 20, 30, tzinfo=pytz.UTC), 'description': 'Debatedores: Marcel Vieira (UFPB), Maria Caú (Globo/UFRJ) e Pablo Gonçalo (UNB) / Mediação: Carolina Amaral'},
            {'name': 'Masterclass: O Medo do Roteirista diante do prazo de entrega', 'date': datetime.datetime(2021, 3, 17, 19, 0, tzinfo=pytz.UTC), 'description': 'Melanie Dimantas'},
            {'name': 'Bate-tela: Roteiro de não-ficção', 'date': datetime.datetime(2021, 3, 17, 20, 30, tzinfo=pytz.UTC), 'description': 'Ana Abreu e Letícia Padilha'},
            {'name': 'Palestra: O ponto de vista do editor sobre o roteiro', 'date': datetime.datetime(2021, 3, 18, 19, 0, tzinfo=pytz.UTC), 'description': 'Eduardo Escorel'},
            {'name': 'Mesa de Debate: Escrita para infantojuvenil', 'date': datetime.datetime(2021, 3, 18, 20, 30, tzinfo=pytz.UTC), 'description': 'Debatedores: Natália Maeda, Renato Nogueira, Thiago Dottori / Mediação: Gell Macedo'},
            {'name': 'Entrevista Primeiro Tratamento', 'date': datetime.datetime(2021, 3, 19, 19, 0, tzinfo=pytz.UTC), 'description': 'Bruno Bloch e Filippo Cordeiro entrevistam Fabio Porchat'},
            {'name': 'Mesa de Debate: Escrevendo roteiros que fogem do realismo', 'date': datetime.datetime(2021, 3, 19, 20, 30, tzinfo=pytz.UTC), 'description': 'Debatedores: Teodoro Poppovic, Felipe Sant Angelo, Mariana Trench Bastos / Mediador: Fernando Ticon'},
            {'name': 'Palestra: Estruturas narrativas não hegemônicas, o que temos a aprender com episódio final de I May Destroy Yoy', 'date': datetime.datetime(2021, 3, 20, 19, 0, tzinfo=pytz.UTC), 'description': 'Maíra de Oliveira'},
            {'name': 'Bate-tela: bíblias de série', 'date': datetime.datetime(2021, 3, 20, 20, 30, tzinfo=pytz.UTC), 'description': 'Myrza e Flávia Vieira'},
            {'name': 'Palestra GEDAR e a questão dos direitos autorais', 'date': datetime.datetime(2021, 3, 21, 11, 0, tzinfo=pytz.UTC), 'description': 'Representante da GEDAR'},
            {'name': 'Por dentro da sala de roteiro', 'date': datetime.datetime(2021, 3, 21, 13, 0, tzinfo=pytz.UTC), 'description': 'Mirna Nogueira'}
        ]

        Seminario.objects.all().delete()
        
        for d in dados:
            Seminario(name=d['name'], date=d['date'], description=d['description']).save()
        
    except Exception as error:
        print('Erro inesperado: {}'.format(repr(error)))