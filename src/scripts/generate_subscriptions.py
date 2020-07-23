from django.contrib.auth.models import User
from core.models import UserProfile
from rota.settings import DEBUG
from essential_generators import DocumentGenerator
import random

QTD = 10
gen = DocumentGenerator()

def clean():
    User.objects.exclude(username='rafapaz@gmail.com').delete()


def gen_roteiro_curta():
    data = {
        'nickname': 
        'phone_home_ddd':
        'phone_home':
        'rg':
        'rg_front':
        'rg_back':
        'cep':
        'address':
        'address_number':
        'address_complement':
        'address_neighborhood':
        'address_city':
        'address_state':
        'title':
        'max_subscriptions':
        'max_pages':
        'coauthors':
        'letter':
        'letter2':
        'is_original':
        'authorize':
        'is_student':
        'script':
        'responsibility':       
    }

    return json.dumps(data)


def gen_data(contest):
    if contest == 1:
        return gen_roteiro_curta()
    
    return None


def run():
    if not DEBUG:
        print('This script cannot be executed in production environment!')
        exit()
    
    clean()

    for i in range(QTD):
        email = gen.email()
        user = User.objects.create_user(
                username=email,
                email=email,
                password='123456',
                first_name=gen.name(),
            )
        
        if not user:
            continue

        UserProfile(
            user=user,
            social_name=gen.word(),
            ddd=str(gen.integer())[:2],
            phone=str(gen.integer())
        ).save()

        sub_data = gen_data(1)

