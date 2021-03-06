import json
from django.shortcuts import render
from core.models import UserProfile, Order, Subscription, Seminario
from django.contrib.auth.models import User


def index(request):
    ups = (UserProfile.objects.select_related('user').all()
           .order_by('auth_user.id'))

    return render(request, 'panel/cadastros/index.html', {
        'ups': ups
    })


def user(request, user_id):
    user = User.objects.get(pk=user_id)
    up = UserProfile.objects.get(user_id=user_id)
    subscriptions = (Subscription.objects.filter(user_id=user_id)
        .order_by('-created_at'))

    for subscription in subscriptions:
        subscription.orders = Order.objects.filter(
            subscription_id=subscription.id)

        subscription.user_data = json.loads(subscription.data)

        if subscription.contest.id == 5:            
            sem_ids = [int(v) for v in subscription.user_data['events'].split(',')]
            subscription.user_data['seminarios'] = Seminario.objects.filter(id__in=sem_ids).all()

    orders = Order.objects.filter(user_id=user_id).order_by('-created_at')

    return render(request, 'panel/cadastros/user.html', {
        'user': user,
        'up': up,
        'subscriptions': subscriptions,
        'total_orders': len(orders),
        'orders': orders,
    })
