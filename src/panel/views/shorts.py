import json
from django.shortcuts import render
from core.models import Subscription, UserRole
from panel.utils import prepara_avaliacao, salva_avaliacao, verifica_indicados


def index(request):
    error = None
    msg = None

    if request.session['painel']['role'][0] == 0:
        items = Subscription.objects.filter(contest_id=4, status=1)
    elif request.session['painel']['role'][0] > 0:
        groups = []
        urs = UserRole.objects.filter(user_id=request.session['painel']['id'], role_id=request.session['painel']['role'][0])
        for ur in urs:
            groups.append(ur.group)

        items = Subscription.objects.filter(contest_id=4, status=1, groups__in=groups).distinct()

    if request.POST:
        error = salva_avaliacao(request.POST, request.session['painel'])
        if not error:
            msg = 'Filme avaliado com sucesso!'

    for item in items:
        item.data = json.loads(item.data) 

    items = prepara_avaliacao(items, request.session['painel'])
    indicados = verifica_indicados(request.session['painel'])

    return render(request, 'panel/shorts/index.html', {
        'items': items,
        'msg': msg,
        'step': request.session['painel']['step'],
        'error': error,
        'indicados': indicados
    })
