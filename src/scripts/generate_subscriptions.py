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
        'caracteristicas_1': random.choice(['ficção', 'documentário', 'mockumentary', 'docudrama', 'outro(s)']),
        'caracteristicas_2': random.choice(['sim', 'não']),
        'caracteristicas_3': random.choice(['curta', 'média', 'longa']),
        'veiculo': random.sample(['Celular', 'Cinema', 'Streaming', 'TV', 'Outros'], random.choice(list(range(1,6)))),
        'genero': random.sample(['Comédia', 'Comédia dramática', 'Drama', 'Dramédia', 'Épico', 'Farsa', 'Histórico', 'Híbrido', 'Musical', 'Tragédia', 'Outro'], random.choice(list(range(1,12)))),
        'logline': gen.sentence(),
        'sinopse': gen.paragraph(),
        'argumento': gen.paragraph(),
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
        'tipo_formato': random.sample(['serializado','procedural','stand','arco aberto','arco fechado','multitrama','antologia','minissérie','outro(s)'], random.choice(list(range(1,10)))),
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
        'url': random.choice(['https://www.youtube.com/watch?v=MkWMkYsGdf0','https://www.youtube.com/watch?v=PkhXLgu-mYM','https://www.youtube.com/watch?v=m8e-FF8MsqU','https://www.youtube.com/watch?v=H-0RHqDWcJE','https://www.youtube.com/watch?v=ggFKLxAQBbc']),
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

        subs = random.choice([1,2,3])
        for i in range(subs):
            sub_id = random.choice([1,2,3,4])
            sub_data = gen_data(sub_id)
            Subscription(user=user, contest_id=sub_id, data=sub_data, status=1).save()

