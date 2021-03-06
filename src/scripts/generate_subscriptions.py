from django.contrib.auth.models import User
from core.models import UserProfile, Subscription, CuradorGroup, Contest
from rota.settings import DEBUG, UPLOAD_DIR
from uuid import uuid4
from essential_generators import DocumentGenerator
import random
import os
import json


CHARS = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
gen = DocumentGenerator()


def clean():
    User.objects.exclude(username='rafapaz@gmail.com').delete() 
    CuradorGroup.objects.all().delete()   
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


def gen_cadastro(name):
    email = gen.email()
    user = User.objects.create_user(
            username=email,
            email=email,
            password='123456',
            first_name=name,
        )
    
    if not user:
        return None

    UserProfile(
        user=user,
        social_name=gen.word(),
        ddd=str(gen.integer())[:2],
        phone=str(gen.integer())[:9]
    ).save()

    return user


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
        'documento_direitos': None if is_original else gen_file(),
        'authorize': random.choice(['sim', 'nao']),
        'is_student': random.choice(['iniciante', 'estudante']),
        'script': gen_file(),
        'responsibility': gen_file()   
    }

    return json.dumps(data)


def gen_encontro():
    pfpj = random.choice(['pf', 'pj'])
    
    data = {
        'phone_home_ddd': str(gen.integer())[:2],
        'phone_home': str(gen.integer())[:9],        
        'cep': str(gen.integer())[:8],
        'address': gen.sentence(),
        'address_number': str(gen.small_int()),
        'address_complement': gen.word(),
        'address_neighborhood': gen.word(),
        'address_city': gen.name(),
        'address_state': gen.word(),
        'pfpj': pfpj,
        'rg': str(gen.integer())[:9] if pfpj == 'pf' else None,
        'cnpj': str(gen.integer())[:14] if pfpj == 'pj' else None,
        'razao_social': gen.name() if pfpj == 'pj' else None,
        'nome_fantasia': gen.name() if pfpj == 'pj' else None,
        'titulo': gen.sentence(),
        'registro_biblioteca': gen_file(),
        'caracteristicas_1': random.choice(['fic????o', 'document??rio', 'mockumentary', 'docudrama', 'outro(s)']),
        'caracteristicas_2': random.choice(['sim', 'n??o']),
        'caracteristicas_3': random.choice(['curta', 'm??dia', 'longa']),
        'veiculo': random.sample(['Celular', 'Cinema', 'Streaming', 'TV', 'Outros'], random.choice(list(range(1,6)))),
        'genero': random.sample(['Com??dia', 'Com??dia dram??tica', 'Drama', 'Dram??dia', '??pico', 'Farsa', 'Hist??rico', 'H??brido', 'Musical', 'Trag??dia', 'Outro'], random.choice(list(range(1,12)))),
        'logline': gen.sentence(),
        'sinopse': gen_file(),
        'argumento': gen_file(),
        'personagens': gen.paragraph(),
        'publico_alvo': gen.paragraph(),
        'biografia': gen.paragraph(),
        'info_adicional': gen.paragraph(),
    }

    return json.dumps(data)


def gen_lab():        
    data = {
        'phone_home_ddd': str(gen.integer())[:2],
        'phone_home': str(gen.integer())[:9],        
        'cep': str(gen.integer())[:8],
        'address': gen.sentence(),
        'address_number': str(gen.small_int()),
        'address_complement': gen.word(),
        'address_neighborhood': gen.word(),
        'address_city': gen.name(),
        'address_state': gen.word(),        
        'rg': str(gen.integer())[:9],
        'rg_front': gen_file(),
        'rg_back': gen_file(),        
        'titulo': gen.sentence(),
        'genero': gen.word(),
        'logline': gen.sentence(),
        'numero_episodios': random.choice(list(range(1,21))),
        'tipo_formato': random.sample(['serializado','procedural','stand','arco aberto','arco fechado','multitrama','antologia','miniss??rie','outro(s)'], random.choice(list(range(1,10)))),
        'conceito': gen.paragraph(),
        'arco_protagonista': gen.paragraph(),
        'universo': gen.paragraph() ,
        'personagens': gen.paragraph(),
        'arco_temporada': gen.paragraph(),
        'temporadas_futuras': gen.paragraph(),
        'sinopse': gen_file(),
        'responsibility': gen_file(),
        'curriculo': gen_file(),
        'registro_biblioteca': gen_file(),
        'documento_direitos': gen_file(),
        'letter': gen_file(),
        'letter2': gen_file()        
    }

    return json.dumps(data)


def gen_mostra():       
    data = {        
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
        'titulo': gen.sentence(),
        'url': random.choice(['https://www.youtube.com/watch?v=MkWMkYsGdf0','https://vimeo.com/394416138','https://youtu.be/4fKyDwBNQF4','https://www.metacafe.com/watch/12106035/','https://www.youtube.com/watch?v=WLHuXQVHXK8&feature=youtu.be']),
        'sinopse': gen.paragraph(),
        'duracao': str(random.choice(list(range(1,21)))) + ' minutos',
        'ano': random.choice([2018, 2019, 2020]),
        'cidade': gen.name(),
        'estado': gen.word(),
        'categoria': random.choice(['1','2']),
        'classificacao': random.choice(['1','2','3','4','5','6']),
        'formato_finalizacao': gen.word(),
        'formato_exibicao': gen.word(),
        'formato_janela': gen.word(),
        'som': gen.word(),
        'cor': random.choice(['1','2']),
        'cpb': gen.word(),
        'site': gen.url(),
        'facebook': gen.url(),
        'festivais': gen.paragraph(),
        'premios': gen.paragraph(),
        'foto_1': gen_file(),
        'foto_2': gen_file(),
        'foto_3': gen_file(),
        'roteirista': gen.name(),
        'max_filmes': 'sim',
        'max_min': 'sim',
        'is_student': random.choice(['iniciante', 'estudante']),
        'responsibility': gen_file(),
        'letter1': gen_file(),
        'letter2': gen_file()
    }

    return json.dumps(data)


def gen_data(contest):
    if contest == 1:
        return gen_roteiro_curta()
    elif contest == 2:
        return gen_encontro()
    elif contest == 3:
        return gen_lab()
    elif contest == 4:
        return gen_mostra()
    
    return None


def run(*args):
    if not DEBUG:
        print('This script cannot be executed in production environment!')
        exit()
        
    if 'clean' in args:
        clean()

    qtd_arg = 0
    for a in args:
        try:
            qtd_arg = int(a)
            break
        except ValueError:
            continue
    
    qtd_sub = dict()
    qtd_sub[1] = 0
    qtd_sub[2] = 0
    qtd_sub[3] = 0
    qtd_sub[4] = 0

    for i in range(qtd_arg):
        user = gen_cadastro(gen.name())
        if user is None:
            continue

        subs = random.choice([1,2,3])
        for i in range(subs):
            contest_id = random.choice([1,2,3,4])
            sub_data = gen_data(contest_id)
            Subscription(user=user, contest_id=contest_id, data=sub_data, status=1).save()
            qtd_sub[contest_id] += 1

    for contest_id, qtd in qtd_sub.items():
        for i in range(int(qtd * 0.05)):
            gen_cadastro('Curador_' + str(User.objects.latest('id').id + 1))

        if 'groups' in args:
            for i in range(5):
                CuradorGroup(contest=Contest.objects.get(id=contest_id), name=CHARS[i]).save()