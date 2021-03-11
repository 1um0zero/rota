from django.contrib.auth.models import User
from core.models import Contest, UserProfile, Subscription, MarcaEncontro
import json
import pandas

def run(*args):
    try:
        #contest_id = int(args[0])
        projects = Subscription.objects.filter(status=1, contest_id=2)
        result = []
               
        for p in projects:
            linha = dict()
            marcacoes = []
            dados = json.loads(p.data)
            user = UserProfile.objects.get(user=p.user)
            linha['Id'] = p.id
            linha['Linha de acao'] = Contest.objects.filter(id=p.contest_id).values('name')[0]['name']
            linha['Projeto'] = dados['title'] if 'title' in dados else dados['titulo']
            linha['Autor'] = p.user.first_name
            linha['Nome social'] = user.social_name
            linha['Estado'] = dados['estado'] if 'estado' in dados else dados['address_state']
            linha['Email'] = p.user.username
            linha['Telefone'] = '({}) {}'.format(user.ddd, user.phone)

            me = MarcaEncontro.objects.filter(subscription_id=p.id, select=True).all()
            for marca in me:
                marcacoes.append(marca.evaluator.first_name)
            
            linha['Players'] = ', '.join(marcacoes)
            result.append(linha)
        
        df = pandas.DataFrame(result)
        
        with pandas.ExcelWriter('report.xlsx') as writer:
            df.to_excel(writer, sheet_name='Encontro')
            
    except Exception as error:
        print('Erro inesperado: {}'.format(repr(error)))