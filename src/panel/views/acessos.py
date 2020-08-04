import json
import random
from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.models import User
from django.db.models import Q, Count
from core.models import Role, UserRole, Subscription, CuradorGroup, Contest

def index(request):
    admins = User.objects.filter(is_superuser=True)
    roles_users = UserRole.objects.all()

    # distribuição de roteiros
    if 'distribute' in request.GET:
        contest_id = int(request.GET.get('contest_id', 1))
        distribute(contest_id)

    res = {}
    for i in [1, 2, 3]:
        res[i] = []
        groups = CuradorGroup.objects.filter(contest_id=i)
        for group in groups:
            res[i].append({
                'group': group,
                'members': UserRole.objects.filter(role_id=1, group=group),
                'roteiros': Subscription.objects.filter(groups__in=[group]).count()
            })

    return render(request, 'panel/acessos/index.html', {
        'admins': admins,
        'roles_users': roles_users,
        'res': res,
    })


def distribute(contest_id):
    subs = Subscription.objects.filter(contest_id=contest_id, status=1, groups=None)
    for sub in subs:
        next_group = get_next_group(contest_id)
        if next_group:
            sub.groups.add(next_group)
            sub.save()
    """
    for sub in subs:
        user_subs = Subscription.objects.filter(user_id=sub.user_id, contest_id=contest_id, status=1, group__isnull=False)
        if user_subs:
            other_groups = get_roteirista_groups(sub.user_id, contest_id)
            curadores_ids = get_curadores_by_groups_ids(other_groups)
            exclude_groups = get_curadores_groups_ids(curadores_ids)
            sub.group_id = get_next_group(contest_id, exclude_groups).id
        else:
            sub.group_id = get_next_group(contest_id).id
        sub.save()
    """

def get_next_group(contest_id):
    grupos = CuradorGroup.objects.filter(contest_id=contest_id, step=1).all()
    if grupos.count() == 0:
        return None

    qtd = []
    for g in grupos:
        qtd.append((g, g.subscription_set.count()))
    qtd.sort(key=lambda x: x[1])

    return qtd[0][0]

"""
def get_roteirista_groups(user_id, contest_id):
    groups_ids = []
    subs = Subscription.objects.filter(contest=Contest.objects.get(id=contest_id), status=1, group__isnull=False,
        user_id=user_id)
    for sub in subs:
        groups_ids.append(sub.group_id)
    return groups_ids


def get_curadores_by_groups_ids(groups_ids):
    curadores_ids = []
    for ur in UserRole.objects.filter(group_id__in=groups_ids):
        if ur.user_id not in curadores_ids:
            curadores_ids.append(ur.user_id)
    return curadores_ids
    

def get_curadores_groups_ids(curadores_ids):
    groups_ids = []
    for curador_id in curadores_ids:
        for ur in UserRole.objects.filter(user_id=curador_id):
            if ur.group_id not in groups_ids:
                groups_ids.append(ur.group_id)
    return groups_ids
"""

"""
def get_next_group(contest_id, exclude=None):
    groups = {}
    query = 'SELECT cg.id, COUNT(s.id) ttl FROM core_curadorgroup cg LEFT JOIN core_subscription s ON s.group_id = cg.id WHERE 1 '
    query += ' AND cg.contest_id = ' + str(contest_id)

    if exclude:
        query += ' AND cg.id NOT IN ({})'.format(','.join([str(cgid) for cgid in exclude]))

    query += ' GROUP BY cg.id ORDER BY ttl, RAND() LIMIT 1'

    subs = Subscription.objects.raw(query)
    if subs:
        sub = subs[0]
        return sub
        
    return random.choice(CuradorGroup.objects.filter(contest=Contest.objects.get(id=contest_id)).all())
"""

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

            return redirect('/painel/acessos')

    return render(request, 'panel/acessos/add.html', {
        'roles': roles,
        'groups': groups,
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
