import json
import random
from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.models import User
from django.db.models import Q, Count
from core.models import Role, UserRole, Subscription, CuradorGroup, Contest, UserProfile

def index(request):
    admins = User.objects.filter(is_superuser=True)
    roles_users = UserRole.objects.all()
    active = int(request.GET.get('active', 1))

    # distribuição de projetos
    if 'distribute' in request.GET:
        contest_id = int(request.GET.get('contest_id', 1))
        distribute(contest_id)

    contests = {}
    for i in [1, 2, 3, 4]:
        contests[i] = []
        groups = CuradorGroup.objects.filter(contest_id=i)
        for group in groups:
            contests[i].append({                
                'group': group,
                'members': UserRole.objects.filter(role_id__gte=1, group=group),
                'roteiros': Subscription.objects.filter(status=1, groups__in=[group]).count()
            })

    return render(request, 'panel/acessos/index.html', {
        'admins': admins,
        'roles_users': roles_users,
        'contests': contests,
        'active': active
    })


def distribute(contest_id):
    subs = Subscription.objects.filter(contest_id=contest_id, status=1, groups=None)
    for sub in subs:
        next_group = get_next_group(contest_id)
        if next_group:
            sub.groups.add(next_group)
            sub.save()
    

def get_next_group(contest_id):
    grupos = CuradorGroup.objects.filter(contest_id=contest_id, step=1).all()
    if grupos.count() == 0:
        return None

    qtd = []
    for g in grupos:
        qtd.append((g, g.subscription_set.filter(status=1).count()))
    qtd.sort(key=lambda x: x[1])

    return qtd[0][0]


def add(request):
    roles = Role.objects.all()
    contest_id = request.GET['contest_id']
    groups = CuradorGroup.objects.filter(contest_id=contest_id)

    if request.POST:
        user_id = int(request.POST['user_id'])
        access = int(request.POST['access'])
        group_id = int(request.POST['group_id'])
        contest_id = int(request.GET['contest_id'])
        
        if user_id > 0 and access > 0 and contest_id > 0:
            ur = UserRole.objects.filter(
                    user_id=user_id,
                    contest_id=contest_id,
                    role_id=access,
                    group_id=group_id,
                )
            if not ur:
                ur = UserRole(
                        user_id=user_id,
                        contest_id=contest_id,
                        role_id=access,
                        group_id=group_id,
                    )
                ur.save()

            return redirect('/painel/acessos?active={}'.format(int(request.GET['active'])))

    return render(request, 'panel/acessos/add.html', {
        'roles': roles,
        'groups': groups,
        'contest_name': Contest.objects.get(id=int(request.GET['contest_id'])).name
    })


def remove(request, ur_id):
    ur = UserRole.objects.get(pk=ur_id)
    ur.delete()
    return redirect('/painel/acessos')


def search(request):
    data = []

    if request.POST:
        user = request.POST['user']
        if user:
            for user in User.objects.filter(Q(email__icontains=user) | Q(first_name__icontains=user))[:10]:                
                data.append({
                    'id': user.id,
                    'name': user.first_name,
                    'email': user.email
                })

    res = HttpResponse(json.dumps(data))
    res['Content-type'] = 'application/json'
    return res
