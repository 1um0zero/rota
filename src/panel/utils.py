import re
import json
import time
import unidecode
from core.models import Subscription, Evaluation
from panel.forms.avaliacao import AvaliacaoConcurso, AvaliacaoConcursoJur, AvaliacaoConcursoCabiria, AvaliacaoLab, AvaliacaoLab2, AvaliacaoMostra, AvaliacaoMostraJur, AvaliacaoMostraSina

ROTEIRO = 1
ENCONTRO = 2
LABORATORIO = 3
MOSTRA = 4

ROLE_CURADOR = 1
ROLE_JURADO = 2
ROLE_CABIRIA = 3
ROLE_SINA = 4
ROLE_PLAYER = 5

FICHAS_AVALIACAO = {
    ROTEIRO: {ROLE_CURADOR: {1: AvaliacaoConcurso}, ROLE_JURADO: {2: AvaliacaoConcursoJur}, ROLE_CABIRIA: {2: AvaliacaoConcursoCabiria} },
    LABORATORIO: {ROLE_CURADOR: {1: AvaliacaoLab, 2: AvaliacaoLab2} },
    MOSTRA: {ROLE_CURADOR: {1: AvaliacaoMostra}, ROLE_JURADO: {2: AvaliacaoMostraJur}, ROLE_SINA: {2: AvaliacaoMostraSina} }
}

INDICACOES_AVALIACAO = {
    ROTEIRO: {ROLE_CURADOR: {1: [(1, 'indica_roteiro', 'Melhor roteiro'), (1,'indica_personagem','Melhor Personagem'), (1,'indica_dialogo','Melhor Diálogo'), (1,'premio_cabiria','Prêmio Cabíria')]}, 
              ROLE_JURADO: {2: [(1, 'indica_roteiro', 'Melhor roteiro'), (1,'indica_personagem','Melhor Personagem'), (1,'indica_dialogo','Melhor Diálogo')]},
              ROLE_CABIRIA: {2: [(1, 'indica_roteiro', 'Melhor protagonista feminina')]} },
    LABORATORIO: {ROLE_CURADOR: {1: [(2, 'indica_projeto', 'Aprovado para a próxima etapa'), (2, 'indica_suplente', 'Suplente')], 
                                 2: [(1, 'indica_projeto', 'Aprovado para a próxima etapa')]} },
    MOSTRA: {ROLE_CURADOR: {1: [(2, 'indica_curta', 'Selecionado para a Mostra'), (2, 'premio_sina', 'Melhor filme com temática social')]}, 
             ROLE_JURADO: {2: [(1, 'indica_ficcao', 'Melhor Ficção'), (1, 'indica_doc', 'Melhor documentário')]}, 
             ROLE_SINA: {2: [(1, 'indica_curta', 'Melhor filme com temática social')]} }
}

def ficha_avaliacao(contest_id, role_id, step):
    try:
        return FICHAS_AVALIACAO[contest_id][role_id][step]
    except:
        return None

def indicacoes_avaliacao(contest_id, role_id, step):
    try:
        return INDICACOES_AVALIACAO[contest_id][role_id][step]
    except:
        return []


def verifica_indicados(sess):
    avaliacoes = Evaluation.objects.filter(evaluator_id=sess['id'], step=sess['step'], role_id=sess['role'][0])
    msg = dict()
    for ind in indicacoes_avaliacao(sess['contest'], sess['role'][0], sess['step']):            
        msg[ind[1]] = []
        
    for a in avaliacoes.all():
        if a.subscription.contest.id != sess['contest']:
            continue
        
        data_indicado = json.loads(a.subscription.data)
        titulo_indicado = data_indicado['title'] if 'title' in data_indicado else data_indicado['titulo']
        questions = json.loads(a.questions)

        for ind in indicacoes_avaliacao(sess['contest'], sess['role'][0], sess['step']):                
            if questions[ind[1]] == 'sim':
                msg[ind[1]].append('{}: {}'.format(ind[2], titulo_indicado.replace('\'',' ').replace('\"','')))

    return msg


def prepara_avaliacao(items, sess):
    ficha = ficha_avaliacao(sess['contest'], sess['role'][0], sess['step'])    
    if ficha is None:
        return items

    for item in items:
        if item.groups is None or sess['role'][0] == 0:
            item.form = ficha()
            continue
                
        msg_indicados_dict = dict()
        item.ja_avaliou = item.evaluation_set.filter(evaluator_id=sess['id'], step=sess['step'], role_id=sess['role'][0]).count()
        outras_avaliacoes = Evaluation.objects.filter(evaluator_id=sess['id'], step=sess['step'], role_id=sess['role'][0]).exclude(subscription_id=item.id)
        qtd_ind = dict()
        msg_aux = dict()
        for ind in indicacoes_avaliacao(sess['contest'], sess['role'][0], sess['step']):            
            qtd_ind[ind[1]] = 0
            msg_aux[ind[1]] = []

        for a in outras_avaliacoes.all():
            if a.subscription.contest.id != item.contest.id:
                continue
            
            data_indicado = json.loads(a.subscription.data)
            titulo_indicado = data_indicado['title'] if 'title' in data_indicado else data_indicado['titulo']
            questions = json.loads(a.questions)
            
            for ind in indicacoes_avaliacao(sess['contest'], sess['role'][0], sess['step']):                
                if questions[ind[1]] == 'sim':
                    qtd_ind[ind[1]] += 1
                    msg_aux[ind[1]].append('{}: {}'.format(ind[2], titulo_indicado.replace('\'',' ').replace('\"','')))
                    if qtd_ind[ind[1]] >= ind[0]:
                        msg_indicados_dict = { **msg_indicados_dict, **{ind[1]:msg_aux[ind[1]]}}                        
        
        item.msg_indicados = json.dumps(msg_indicados_dict)
        try:
            avaliacao = Evaluation.objects.get(subscription=item, evaluator_id=sess['id'], step=sess['step'])
            grades = json.loads(avaliacao.grades if avaliacao.grades else '{}')
            questions = json.loads(avaliacao.questions)
            item.form = ficha(initial={**grades , **questions})            
        except:
            item.form = ficha()

    return items


def salva_avaliacao(post, sess):
    ficha = ficha_avaliacao(sess['contest'], sess['role'][0], sess['step'])
    form = ficha(post)
    if form.is_valid():
        grades = dict()
        questions = dict()
        for g in form.get_grades():
            grades[g] = form.cleaned_data.get(g)
        for q in form.get_questions():
            questions[q] = form.cleaned_data.get(q)
        
        subscription = Subscription.objects.get(id=int(post['sub_id']))
        evaluation, created = Evaluation.objects.update_or_create(subscription=subscription, evaluator_id=sess['id'],
                                role_id=sess['role'][0], step=sess['step'], 
                                defaults={'grades': json.dumps(grades), 'questions': json.dumps(questions)})
        time.sleep(1)
        return None
    else:
        return form.errors


def make_url(title):
    title = title.lower()
    title = unidecode.unidecode(title)
    title = title.replace(' ', '-')
    title = re.sub('([^a-zA-Z0-9-_]+)', '-', title)
    title = re.sub('^-', '', title)
    title = re.sub('-$', '', title)
    while '--' in  title:
        title = title.replace('--', '-')
    return title
