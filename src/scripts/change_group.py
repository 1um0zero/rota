from django.contrib.auth.models import User
from core.models import UserProfile, Subscription, CuradorGroup, Evaluation, UserRole
import os


def run(*args):
    try:
        sub_id = int(args[0])
        g1_nome = args[1]
        g2_nome = args[2]

        s = Subscription.objects.get(id=sub_id)
        g1 = CuradorGroup.objects.get(contest_id=s.contest_id, name=g1_nome)
        g2 = CuradorGroup.objects.get(contest_id=s.contest_id, name=g2_nome)
        evals = Evaluation.objects.filter(subscription=s, step=1)

        for e in evals.all():
            user_role = UserRole.objects.get(user=e.evaluator, role=e.role)
            if user_role.group.id == g1.id:
                print('Removendo avaliação de {}'.format(e.evaluator))
                e.delete()

        print('Antes: {}'.format(s.groups.only('name')))
        s.groups.remove(g1)
        s.groups.add(g2)
        s.save()
        print('Depois: {}'.format(s.groups.only('name')))

    except Exception as error:
        print('Erro inesperado: {}'.format(repr(error)))