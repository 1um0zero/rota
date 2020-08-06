import json
from django.shortcuts import render
from core.models import Subscription, UserRole


def index(request):
    if request.session['painel']['role'][0] == 0:
        items = Subscription.objects.filter(contest_id=4, status=1)
    elif request.session['painel']['role'][0] > 0:
        groups = []
        urs = UserRole.objects.filter(user_id=request.session['painel']['id'], role_id=request.session['painel']['role'][0])
        for ur in urs:
            groups.append(ur.group)

        items = Subscription.objects.filter(contest_id=4, status=1, groups__in=groups).distinct()

    for item in items:
        item.user_data = json.loads(item.data) 

    return render(request, 'panel/shorts/index.html', {
        'shorts': items
    })
