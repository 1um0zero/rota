import json
from statistics import mean
from django.shortcuts import render, HttpResponse
from core.models import Evaluation, Subscription

def index(request):
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
                avaliadores.append(av.evaluator.first_name)
            
            if len(notas) == 0:
                continue

            media = mean(notas)
            cat['projetos'].append({'id': insc.id, 'data': json.loads(insc.data), 'autor': insc.user.first_name, 'media': media, 'avaliadores': avaliadores})

        if len(cat['projetos']) > 0:
            cat['projetos'].sort(reverse=True, key=lambda x: x['media'])

    context = {'categorias_roteiro_1': categorias_roteiro_1}
    return render(request, 'panel/avaliacoes/ranking.html', context=context)