import json
from statistics import mean
from django.shortcuts import render, HttpResponse
from core.models import Evaluation, Subscription, UserProfile
from panel.utils import indicacoes_avaliacao, ROTEIRO, LABORATORIO, MOSTRA, ROLE_CURADOR, ROLE_JURADO, ROLE_CABIRIA, ROLE_SINA, ROLE_PLAYER


def index(request):
    res = dict()
    for contest_id in [ROTEIRO, LABORATORIO, MOSTRA]:
        res[contest_id] = dict()
        inscricoes = Subscription.objects.filter(status=1, contest_id=contest_id)
        for step in [1,2]:
            res[contest_id][step] = []
            for role_id in [ROLE_CURADOR, ROLE_JURADO, ROLE_CABIRIA, ROLE_SINA, ROLE_PLAYER]:
                categorias = indicacoes_avaliacao(contest_id, role_id, step)
                for cat in categorias:
                    projetos_lst = []                    
                    for insc in inscricoes:
                        media = 0            
                        notas = []
                        avaliadores = []

                        for av in insc.evaluation_set.filter(step=step, role_id=role_id):
                            questoes = json.loads(av.questions)
                            if questoes[cat[1]] == 'nao':
                                continue
                            notas.append(sum([v for k,v in json.loads(av.grades).items()]))
                            avaliador_profile = UserProfile.objects.get(user=av.evaluator)
                            avaliadores.append(avaliador_profile.get_name())

                        if len(avaliadores) == 0:
                            continue

                        if len(notas) > 0:
                            media = mean(notas)
                        user_profile = UserProfile.objects.get(user=insc.user)                        
                        projetos_lst.append({'id': insc.id, 'data': json.loads(insc.data), 'autor': user_profile.get_name(), 'media': media, 'avaliadores': avaliadores})

                    if len(projetos_lst) > 0:
                        projetos_lst.sort(reverse=True, key=lambda x: (len(x['avaliadores']), x['media']))    
                    res[contest_id][step].append({'categoria': cat, 'projetos': projetos_lst})
    
    return render(request, 'panel/avaliacoes/ranking.html', context={'res': res})
                        


def lixo_apagar(request):
    categorias_roteiro_1 = [
        {'campo':'indica_roteiro', 'nome': 'Melhor Roteiro'},
        {'campo':'indica_personagem', 'nome': 'Melhor Personagem'},
        {'campo':'indica_dialogo', 'nome': 'Melhor Diálogo'},
        {'campo':'premio_cabiria', 'nome': 'Melhor Protagonista Feminina (Prêmio Cabíria)'},
    ]

    for cat in categorias_roteiro_1:        
        inscricoes = Subscription.objects.filter(status=1, contest_id=1)
        cat['projetos'] = []
        for insc in inscricoes:            
            media = 0            
            notas = []
            avaliadores = []

            for av in insc.evaluation_set.filter(step=1, role_id=1):
                questoes = json.loads(av.questions)
                if questoes[cat['campo']] == 'nao':
                    continue

                notas.append(sum([v for k,v in json.loads(av.grades).items()]))
                user_profile = UserProfile.objects.get(user=av.evaluator)
                avaliadores.append(user_profile.get_name())
            
            if len(notas) == 0:
                continue

            media = mean(notas)
            user_profile = UserProfile.objects.get(user=insc.user)
            cat['projetos'].append({'id': insc.id, 'data': json.loads(insc.data), 'autor': user_profile.get_name(), 'media': media, 'avaliadores': avaliadores})

        if len(cat['projetos']) > 0:
            cat['projetos'].sort(reverse=True, key=lambda x: x['media'])

    context = {'categorias_roteiro_1': categorias_roteiro_1}
    return render(request, 'panel/avaliacoes/ranking.html', context=context)