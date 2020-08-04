import os
import json
from django.shortcuts import render, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from core.models import Script, Subscription, UserRole, Folder
from rota.settings import UPLOAD_DIR


def index(request):
    
    items = None
    folder = None
    folders = None
    path = '<a href="/painel/encontro"><i class="fa fa-home"></i></a> '

    if 'f' in request.GET:
        folder = Folder.objects.get(pk=int(request.GET['f']))

    if folder:
        folders = Folder.objects.filter(parent_id=folder.id)
        _path = [folder]
        _f = folder

        while _f.parent_id:
            _f = Folder.objects.get(pk=_f.parent_id)
            _path.append(_f)
        _path.reverse()
        
        for _p in _path:
            path += ' <strong>/</strong> <a href="/painel/encontro?f={}">{}</a>'.format(
                _p.id, _p.name)

    else:
        folders = Folder.objects.filter(parent_id__isnull=True)
        path += ' <strong>/</strong> '

    for _f in folders:
        qtd = Subscription.objects.filter(folder_id=_f.id).count()
        folders

    if not folders:
        if request.session['painel']['role'][0] == 0:
            items = Subscription.objects.filter(contest_id=2, status=1, folder_id=folder.id if folder is not None else 0)

        elif request.session['painel']['role'][0] > 0:
            groups = []
            urs = UserRole.objects.filter(user_id=request.session['painel']['id'], role_id=request.session['painel']['role'][0])
            for ur in urs:
                groups.append(ur.group)

            items = Subscription.objects.filter(contest_id=2, status=1, groups__in=groups, folder_id=folder.id).distinct()

        for item in items:
            item.data = json.loads(item.data)

    return render(request, 'panel/encontro/index.html', {
        'folder': folder,
        'folders': folders,
        'items': items,
        'path': path
    })


def view(request, project_id):
    subscription = Subscription.objects.get(
        pk=project_id, contest_id=2, status=1)

    subscription.user_data = json.loads(subscription.data)

    return render(request, 'panel/encontro/view.html', {
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

@csrf_exempt
def folders(request):
    parent_id = None
    if 'f' in request.GET:
        parent_id = int(request.GET['f'])

    if 'subscription_id' in request.POST:
        sub_id = int(request.POST['subscription_id'])
        folder_id = int(request.POST['folder_id'])
        sub = Subscription.objects.get(pk=sub_id)
        sub.folder_id = folder_id
        sub.save()


    if not parent_id:
        folders = Folder.objects.filter(parent_id__isnull=True)
    else:
        folders = Folder.objects.filter(parent_id=parent_id)

    res = [{'id': folder.id, 'name': folder.name} for folder in folders]

    return HttpResponse(json.dumps(res))

