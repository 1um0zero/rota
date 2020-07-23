from django.contrib.auth.models import User
from core.models import UserProfile, Subscription
from rota.settings import DEBUG, UPLOAD_DIR
from uuid import uuid4
from essential_generators import DocumentGenerator
import random
import os
import json

QTD = 100
gen = DocumentGenerator()


def clean():
    User.objects.exclude(username='rafapaz@gmail.com').delete()    
    for filename in os.listdir(UPLOAD_DIR):
        try:
            file_path = os.path.join(UPLOAD_DIR, filename)
            os.unlink(file_path)
        except Exception as e:
            print('Failed to delete %s. Reason: %s' % (file_path, e))

def gen_file():
    filename = str(uuid4())
    path = os.path.join(UPLOAD_DIR, filename)
    with open(path, 'wb') as _f:
        _f.write(b'00')
    
    newpath = path + '.pdf'
    os.rename(path, newpath)
    return filename + '.pdf'


def gen_roteiro_curta():
    coautor = random.choice([True, False])
    is_original = random.choice([True, False])

    data = {
        'nickname': gen.word(),
        'phone_home_ddd': str(gen.integer())[:2],
        'phone_home': str(gen.integer())[:9],
        'rg': str(gen.integer())[:9],
        'rg_front': gen_file(),
        'rg_back': gen_file(),
        'cep': str(gen.integer())[:8],
        'address': gen.sentence(),
        'address_number': str(gen.small_int()),
        'address_complement': gen.word(),
        'address_neighborhood': gen.word(),
        'address_city': gen.name(),
        'address_state': gen.word(),
        'title': gen.sentence(),
        'max_subscriptions': 'sim',
        'max_pages': 'sim',
        'coauthors': 'sim' if coautor else 'nao',
        'letter': gen_file() if coautor else None,
        'letter2': gen_file() if coautor else None,
        'is_original': 'original' if is_original else 'adaptado',
        'authorize': random.choice(['sim', 'nao']),
        'is_student': random.choice(['iniciante', 'estudante']),
        'script': gen_file(),
        'responsibility': gen_file()   
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
            phone=str(gen.integer())[:9]
        ).save()

        sub_id = random.choice([1])
        sub_data = gen_data(sub_id)
        Subscription(user=user, contest_id=sub_id, data=sub_data, status=1).save()

