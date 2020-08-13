import json
from statistics import mean
from django.shortcuts import render, HttpResponse, redirect
from core.models import Evaluation, Subscription, UserProfile, CuradorGroup
from panel.utils import indicacoes_avaliacao, ficha_avaliacao, ROTEIRO, LABORATORIO, MOSTRA, ROLE_CURADOR, ROLE_JURADO, ROLE_CABIRIA, ROLE_SINA


def index(request):
    res = dict()
    outros = dict()
    for contest_id in [ROTEIRO, LABORATORIO, MOSTRA]:
        res[contest_id] = dict()
        outros[contest_id] = dict()
        inscricoes = Subscription.objects.filter(status=1, contest_id=contest_id)
        for step in [1,2]:
            res[contest_id][step] = []
            outros[contest_id][step] = []
            for role_id in [ROLE_CURADOR, ROLE_JURADO, ROLE_CABIRIA, ROLE_SINA]:
                categorias = indicacoes_avaliacao(contest_id, role_id, step)
                cat_projetos = dict()
                for insc in inscricoes:
                    if insc.evaluation_set.filter(step=step, role_id=role_id).count() == 0:
                        continue

                    media = 0
                    notas = []
                    avaliadores = []
                    indicacoes = []
                    
                    #user_profile = UserProfile.objects.get(user=insc.user)
                    user_data = json.loads(insc.data)
                    if 'titulo' in user_data:
                        user_data['title'] = user_data['titulo']

                    for av in insc.evaluation_set.filter(step=step, role_id=role_id):
                        if av.grades:
                            notas.append(sum([v for k,v in json.loads(av.grades).items()]))                        
                        avaliador_profile = UserProfile.objects.get(user=av.evaluator)
                        avaliadores.append(avaliador_profile.get_name())
                        questoes = json.loads(av.questions)
                        for cat in categorias:                            
                            if questoes[cat[1]] == 'sim':
                                indicacoes.append((cat, avaliador_profile.get_name()))                                
                    
                    if len(notas) > 0:
                        media = mean(notas)

                    if len(indicacoes) == 0:
                        projeto = {'id': insc.id, 'data': user_data, 'cadastro': insc.user.id, 'media': media, 'avaliadores': avaliadores, 'indicadores': []}
                        ja_tem = False
                        for p in outros[contest_id][step]:
                            if p['id'] == projeto['id']:
                                p['media'] = max(p['media'], media)
                                p['avaliadores'] += avaliadores
                                ja_tem = True

                        if not ja_tem:
                            outros[contest_id][step].append(projeto)
                        continue
                    
                    for cat in categorias:
                        indicadores = []
                        if cat[1] not in cat_projetos:
                            cat_projetos[cat[1]] = []
                        for ind in indicacoes:
                            if ind[0][1] == cat[1]:
                                indicadores.append(ind[1])
                        if len(indicadores) > 0:
                            projeto = {'id': insc.id, 'data': user_data, 'cadastro': insc.user.id, 'media': media, 'avaliadores': avaliadores, 'indicadores': indicadores}
                            cat_projetos[cat[1]].append(projeto)
                        
                if len(outros[contest_id][step]) > 0:
                    outros[contest_id][step].sort(reverse=True, key=lambda x: x['media'])

                for cat in categorias:
                    if cat[1] in cat_projetos:
                        cat_projetos[cat[1]].sort(reverse=True, key=lambda x: (len(x['indicadores']), x['media']))
                        res[contest_id][step].append({'categoria': cat, 'projetos': cat_projetos[cat[1]]})

    return render(request, 'panel/avaliacoes/ranking.html', context={'res': res, 'outros': outros})


def ficha(request, sub_id):
    sub = Subscription.objects.get(id=sub_id)
    user_data = json.loads(sub.data)
    if 'titulo' in user_data:
        user_data['title'] = user_data['titulo']
    sub.data = user_data
    fichas = []
    for av in sub.evaluation_set.all():
        ficha_form = ficha_avaliacao(sub.contest_id, av.role_id, av.step)
        grades = json.loads(av.grades if av.grades else '{}')
        questions = json.loads(av.questions)
        form = ficha_form(initial={**grades , **questions})
        avaliador_profile = UserProfile.objects.get(user=av.evaluator)        
        fichas.append({'step': av.step, 'form': form, 'role_name': av.role.name, 'avaliador': avaliador_profile.get_name()})
    return render(request, 'panel/avaliacoes/fichas.html', {'sub': sub, 'fichas': fichas})


def promover(request):
    selecionados = [int(x) for x in set(request.POST['selecionados'].split(','))]
    step = int(request.POST['step'])
    qtd_grupos = int(request.POST['qtd_grupos'])
    prefixo = request.POST['grupo_prefixo']
    contest = Subscription.objects.get(id=selecionados[0]).contest

    ppg = [[] for i in range(qtd_grupos)] # projetos por grupo. Ex: [[p1,p2],[p3,p4],[p5]]    
    i = 0
    while len(selecionados) > 0:
        ppg[i % qtd_grupos].append(selecionados.pop())
        i += 1

    for i in range(qtd_grupos):
        grupo = CuradorGroup(contest=contest, name='{}_{}'.format(prefixo, i+1), step=step)
        grupo.save()
        for sub_id in ppg[i]:
            sub = Subscription.objects.get(id=sub_id)
            sub.groups.add(grupo)
            sub.save()
    
    return redirect('/painel/acessos')