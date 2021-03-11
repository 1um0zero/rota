from django.contrib.auth.models import User
from core.models import Contest, UserProfile, Subscription
import json
import pandas

def run(*args):
    try:
        #contest_id = int(args[0])
        users = UserProfile.objects.all()
        result = []
                
        for u in users:
            linha = dict()            
            linha['Nome'] = u.user.first_name
            linha['Nome social'] = u.social_name            
            linha['Email'] = u.user.username
            linha['Telefone'] = '({}) {}'.format(u.ddd, u.phone)
            result.append(linha)
            
        df = pandas.DataFrame(result)
        
        with pandas.ExcelWriter('report.xlsx') as writer:
            df.to_excel(writer, sheet_name='Inscritos')            

    except Exception as error:
        print('Erro inesperado: {}'.format(repr(error)))