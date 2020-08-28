import json
from django.shortcuts import render
from core.models import Subscription, UserRole, UserProfile
from panel.utils import prepara_avaliacao, salva_avaliacao, verifica_indicados


def index(request):
    error = None
    msg = None
    groups = []

    if request.session['painel']['role'][0] == 0:
        items = Subscription.objects.filter(contest_id=4, status=1)
        g_aux = []
        for i in items:
            g_aux += i.groups.all()
        groups = list(set(g_aux)) 

    elif request.session['painel']['role'][0] > 0:        
        urs = UserRole.objects.filter(user_id=request.session['painel']['id'], role_id=request.session['painel']['role'][0])
        for ur in urs:
            groups.append(ur.group)

        items = Subscription.objects.filter(contest_id=4, status=1, groups__in=groups).distinct()

    if request.POST:
        error = salva_avaliacao(request.POST, request.session['painel'])
        if not error:
            msg = 'Filme avaliado com sucesso!'

    for item in items:
        user_profile = UserProfile.objects.get(user=item.user)
        item.social_name = user_profile.get_name()
        item.data = json.loads(item.data) 

    items = prepara_avaliacao(items, request.session['painel'])
    indicados = verifica_indicados(request.session['painel'])
    for item in items:
        item.groups_str = [g.name for g in item.groups.all()]
    for g in groups:        
        g.membros = [(UserProfile.objects.get(user=ur.user)).get_name() for ur in g.userrole_set.all()]
    groups.sort(key=lambda x: x.name)
    
    return render(request, 'panel/shorts/index.html', {
        'items': items,
        'msg': msg,
        'step': request.session['painel']['step'],
        'groups': groups,
        'error': error,
        'indicados': indicados
    })
