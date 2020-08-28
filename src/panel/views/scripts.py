import os
import json
import time
from django.shortcuts import render, HttpResponse
from core.models import Script, Subscription, UserRole, Evaluation, UserProfile
from panel.utils import prepara_avaliacao, salva_avaliacao, verifica_indicados
from rota.settings import UPLOAD_DIR


def index(request):
    error = None
    msg = None
    groups = []
            
    if request.session['painel']['role'][0] == 0:
        items = Subscription.objects.filter(contest_id=1, status=1)
        g_aux = []
        for i in items:
            g_aux += i.groups.all()
        groups = list(set(g_aux)) 

    elif request.session['painel']['role'][0] > 0:        
        urs = UserRole.objects.filter(user_id=request.session['painel']['id'], role_id=request.session['painel']['role'][0])
        for ur in urs:
            groups.append(ur.group)

        items = Subscription.objects.filter(contest_id=1, status=1, groups__in=groups).distinct()
            
    if request.POST:
        error = salva_avaliacao(request.POST, request.session['painel'])
        if not error:
            msg = 'Roteiro avaliado com sucesso!'
    
    for item in items:
        item.data = json.loads(item.data)

    items = prepara_avaliacao(items, request.session['painel'])
    indicados = verifica_indicados(request.session['painel'])
    for item in items:
        item.groups_str = [g.name for g in item.groups.all()]
    for g in groups:        
        g.membros = [(UserProfile.objects.get(user=ur.user)).get_name() for ur in g.userrole_set.all()]
    groups.sort(key=lambda x: x.name)
    
    return render(request, 'panel/scripts/index.html', {
        'items': items,
        'msg': msg,
        'step': request.session['painel']['step'],
        'groups': groups,
        'error': error,
        'indicados': indicados
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
