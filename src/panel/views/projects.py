import os
import json
from django.shortcuts import render, HttpResponse
from core.models import Script, Subscription, UserRole
from rota.settings import UPLOAD_DIR


def index(request):
    
    if request.session['painel']['role'][0] == 0:

        items = Subscription.objects.filter(contest_id=3, status=1)

    elif request.session['painel']['role'][0] == 1:
        groups_ids = []
        urs = UserRole.objects.filter(user_id=request.session['painel']['id'],
            role_id=1)
        for ur in urs:
            groups_ids.append(ur.group_id)

        items = Subscription.objects.filter(contest_id=3, status=1,
            group_id__in=groups_ids)

    for item in items:
        item.data = json.loads(item.data)
    return render(request, 'panel/projects/index.html', {
        'items': items
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
