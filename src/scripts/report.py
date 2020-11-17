from django.contrib.auth.models import User
from core.models import UserProfile, Subscription
import json
import pandas

def run(*args):
    try:
        contest_id = int(args[0])
        projects = Subscription.objects.filter(contest_id=contest_id, status=1)
        result = []
        for p in projects:
            linha = dict()
            dados = json.loads(p.data)
            user = UserProfile.objects.get(user=p.user)
            linha['Id'] = p.id
            linha['Projeto'] = dados['title'] if 'title' in dados else dados['titulo']
            linha['Autor'] = p.user.first_name
            linha['Nome social'] = user.social_name
            linha['Email'] = p.user.username
            linha['Telefone'] = '({}) {}'.format(user.ddd, user.phone)
            result.append(linha)

        df = pandas.DataFrame(result)
        df.to_excel("report.xlsx")
    except Exception as error:
        print('Erro inesperado: {}'.format(repr(error)))