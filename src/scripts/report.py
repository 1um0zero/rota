from django.contrib.auth.models import User
from core.models import Contest, UserProfile, Subscription
import json
import pandas

def run(*args):
    try:
        #contest_id = int(args[0])
        projects = Subscription.objects.filter(status=1)
        result = []
        resumo = []
        contador_estado = dict()
        autores = set()
        
        for p in projects:
            linha = dict()
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
            result.append(linha)
            if linha['Autor'] not in autores:
                if linha['Estado'] in contador_estado:
                    contador_estado[linha['Estado']] += 1
                else:
                    contador_estado[linha['Estado']] = 0

            autores.add(linha['Autor'])

        for k, v in contador_estado.items():
            linha = dict()
            linha['Estado'] = k
            linha['Qtd'] = v
            resumo.append(linha)

        df = pandas.DataFrame(result)
        df_resumo = pandas.DataFrame(resumo)

        with pandas.ExcelWriter('report.xlsx') as writer:
            df.to_excel(writer, sheet_name='Inscritos')
            df_resumo.to_excel(writer, sheet_name='Total por estado')

    except Exception as error:
        print('Erro inesperado: {}'.format(repr(error)))