import os
import json
from django.contrib.auth.models import User
from django.shortcuts import render, HttpResponse, redirect
from django.views.decorators.csrf import csrf_exempt
from core.models import Subscription, Seminario
from rota.settings import UPLOAD_DIR


def index(request):
    palestras = []

    subscriptions = Subscription.objects.filter(contest_id=5)
    seminarios = Seminario.objects.all()

    for s in seminarios:
        linha = dict()
        linha['evento'] = s
        linha['qtd'] = 0
        linha['pessoas'] = []
        for i in subscriptions:
            data = json.loads(i.data)
            sem_ids = [int(v) for v in data['events'].split(',')]
            if s.id in sem_ids:
                linha['qtd'] += 1
                linha['pessoas'].append(i.user)
        palestras.append(linha)

    return render(request, 'panel/seminario/index.html', {
        'palestras': palestras
    })