import os
import json
from django.shortcuts import render, HttpResponse
from core.models import Script, Subscription, UserRole
from panel.utils import prepara_avaliacao, salva_avaliacao, verifica_indicados
from rota.settings import UPLOAD_DIR


def index(request):
    error = None
    msg = None
    
    if request.session['painel']['role'][0] == 0:
        items = Subscription.objects.filter(contest_id=3, status=1)

    elif request.session['painel']['role'][0] > 0:
        groups = []
        urs = UserRole.objects.filter(user_id=request.session['painel']['id'], role_id=request.session['painel']['role'][0])
        for ur in urs:
            groups.append(ur.group)

        items = Subscription.objects.filter(contest_id=3, status=1, groups__in=groups).distinct()

    if request.POST:
        error = salva_avaliacao(request.POST, request.session['painel'])
        if not error:
            msg = 'Projeto avaliado com sucesso!'

    for item in items:
        item.data = json.loads(item.data)
    
    items = prepara_avaliacao(items, request.session['painel'])
    indicados = verifica_indicados(request.session['painel'])

    return render(request, 'panel/projects/index.html', {
        'items': items,
        'msg': msg,
        'step': request.session['painel']['step'],
        'error': error,
        'indicados': indicados
    })


def view(request, project_id):
    subscription = Subscription.objects.get(
        pk=project_id, contest_id=3, status=1)

    subscription.user_data = json.loads(subscription.data)

    return render(request, 'panel/projects/view.html', {
        'subscription': subscription
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
