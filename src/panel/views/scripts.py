import os
import json
import time
from django.shortcuts import render, HttpResponse
from core.models import Script, Subscription, UserRole, Evaluation
from panel.forms.avaliacao import AvaliacaoConcurso
from rota.settings import UPLOAD_DIR


def index(request):
    error = None
    msg = None
    ja_avaliou = None
        
    if request.session['painel']['role'][0] == 0:
        items = Subscription.objects.filter(contest_id=1, status=1)
    elif request.session['painel']['role'][0] > 0:
        groups = []
        urs = UserRole.objects.filter(user_id=request.session['painel']['id'], role_id=request.session['painel']['role'][0])
        for ur in urs:
            groups.append(ur.group)

        items = Subscription.objects.filter(contest_id=1, status=1, groups__in=groups).distinct()
            
    if request.POST:        
        form = AvaliacaoConcurso(request.POST)
        if form.is_valid():
            grades = dict()
            questions = dict()
            for g in form.get_grades():
                grades[g] = form.cleaned_data.get(g)
            for q in form.get_questions():
                questions[q] = form.cleaned_data.get(q)
            
            subscription = Subscription.objects.get(id=int(request.POST['sub_id']))
            evaluation, created = Evaluation.objects.update_or_create(subscription=subscription, evaluator_id=request.session['painel']['id'],
                                    role_id=request.session['painel']['role'][0], step=request.session['painel']['step'], 
                                    defaults={'grades': json.dumps(grades), 'questions': json.dumps(questions)})
            time.sleep(1)
            msg = "Roteiro avaliado com sucesso!"
        else:
            error = form.errors
    
    for item in items:
        item.data = json.loads(item.data)
        
        if item.groups is None or request.session['painel']['role'][0] == 0:
            item.form = AvaliacaoConcurso()
            continue
        
        item.ja_avaliou = item.evaluation_set.filter(evaluator_id=request.session['painel']['id'], step=request.session['painel']['step'], role_id=request.session['painel']['role'][0]).count()
        outras_avaliacoes = Evaluation.objects.filter(evaluator_id=request.session['painel']['id'], step=request.session['painel']['step'], role_id=request.session['painel']['role'][0])
        for a in outras_avaliacoes.all():
            if a.subscription.contest.id != item.contest.id or a.subscription.id == item.id:
                continue

            titulo_indicado = json.loads(a.subscription.data)['title']            
            questions = json.loads(a.questions)
            if questions['indica_roteiro'] == 'sim':
                item.msg_indicado_roteiro = 'Melhor roteiro: {}'.format(titulo_indicado.replace('\'',' '))
            if questions['indica_personagem'] == 'sim':
                item.msg_indicado_personagem = 'Melhor Personagem: {}'.format(titulo_indicado.replace('\'',' '))
            if questions['indica_dialogo'] == 'sim':
                item.msg_indicado_dialogo = 'Melhor Diálogo: {}'.format(titulo_indicado.replace('\'',' '))
            if questions['premio_cabiria'] == 'sim':
                item.msg_premio_cabiria = 'Prêmio Cabíria: {}'.format(titulo_indicado.replace('\'',' '))

        try:
            avaliacao = Evaluation.objects.get(subscription=item, evaluator_id=request.session['painel']['id'], step=request.session['painel']['step'])
            grades = json.loads(avaliacao.grades)
            questions = json.loads(avaliacao.questions)            
            item.form = AvaliacaoConcurso(initial={**grades , **questions})            
        except:
            item.form = AvaliacaoConcurso()

    return render(request, 'panel/scripts/index.html', {
        'items': items,
        'msg': msg,
        'step': request.session['painel']['step'],
        'error': error
    })


def download(request, script_id):
    script = Script.objects.get(pk=script_id)
    path = os.path.join(UPLOAD_DIR, script.filename)

    with open(path, 'rb') as _f:
        content = _f.read()
    
    response = HttpResponse(content)
    response['Content-Disposition'] = 'attachment; filename="{}"'.format(
        script.original_filename
    )

    return response
