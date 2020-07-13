from django.db.models import Sum
from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from core.models import Subscription, Order, UserRole
from datetime import datetime, timedelta


def admin_login(request):

    error_msg = None

    if request.session.get('painel'):
        return redirect('/painel')

    if request.POST:
        email = request.POST['email']
        password = request.POST['password']

        user = authenticate(request, username=email, password=password)
        role = None
        contest_ids = []

        if user:
            if user.is_superuser:
                role = (0, 'Administrador(a)')
            else:
                ur = UserRole.objects.filter(user_id=user.id)
                if ur:
                    role = (ur[0].role.id, ur[0].role.name)
                    for u in ur:
                        contest_ids.append(u.contest_id)
        
        if role:
            request.session['painel'] = {
                'id': user.id,
                'email': user.email,
                'name': user.first_name,
                'role': role,
                'is_admin': role[0] == 0,
                'is_curador': role[0] == 1,
                'view_roteiros': 1 in contest_ids,
                'view_encontro': 2 in contest_ids,
                'view_projetos': 3 in contest_ids,
            }
            
            url = ''
            if request.session['painel']['is_curador']:
                if request.session['painel']['view_projetos']:
                    url = '/projetos'
                elif request.session['painel']['view_encontro']:
                    url = '/encontro'
                else:
                    url = '/roteiros'

            return redirect('/painel' + url)
        else:
            error_msg = 'Email ou senha inválidos.'
        

    return render(request, 'panel/login.html', {
        'error_msg': error_msg
    })

def admin_logout(request):
    if request.session.get('painel'):
        logout(request)
        request.session['painel'] = False
        return redirect('/painel/login')

def index(request):

    if not request.session['painel']['is_admin']:
        if ('view_projetos' in request.session['painel']
                and request.session['painel']['view_projetos']):
            return redirect('/painel/projetos')
        elif ('view_encontro' in request.session['painel']
                and request.session['painel']['view_encontro']):
            return redirect('/painel/encontro')
        return redirect('/painel/roteiros')

    qt_users = User.objects.all().count()

    qt_subscriptions = Subscription.objects.all().count()
    pct_subscriptions = round(qt_subscriptions / qt_users * 100, 2)

    qt_orders = Order.objects.all().count()
    pct_orders = round(qt_orders / qt_subscriptions * 100 if qt_subscriptions else 0.0, 2)

    qt_payments = Order.objects.filter(status=3).count()
    pct_payments = round(qt_payments / qt_orders * 100 if qt_orders else 0.0, 2)

    last_subscriptions = Subscription.objects.all().order_by('-created_at')[:10]

    chart_period = 15

    today = datetime.now().strftime('%d/%m/%Y')
    two_weeks = (datetime.now() - timedelta(days=chart_period)).strftime('%d/%m/%Y')

    chart_labels = []
    chart_users = []
    chart_subscriptions = []
    chart_orders = []
    chart_payments = []

    for i in range(chart_period + 1):

        date = (datetime.now() - timedelta(days=chart_period - i))
        chart_labels.append(date.strftime('%d/%m'))

        qtd = User.objects.filter(date_joined__startswith=date.strftime('%Y-%m-%d ')).count()
        chart_users.append(qtd)

        qtd = Subscription.objects.filter(created_at__startswith=date.strftime('%Y-%m-%d ')).count()
        chart_subscriptions.append(qtd)

        qtd = Order.objects.filter(created_at__startswith=date.strftime('%Y-%m-%d ')).count()
        chart_orders.append(qtd)

        qtd = Order.objects.filter(created_at__startswith=date.strftime('%Y-%m-%d '),
            status=3).count()
        chart_payments.append(qtd)
    
    totals = {'users': 0, 'subscriptions': 0, 'orders': 0, 'payments': 0}


    for i in chart_users:
        totals['users'] += i
    for i in chart_subscriptions:
        totals['subscriptions'] += i
    for i in chart_orders:
        totals['orders'] += i
    for i in chart_payments:
        totals['payments'] += i

    biggest = max(totals['users'], totals['subscriptions'], totals['orders'],
        totals['payments'])
    
    if biggest > 0:
        totals['users_pct'] = int(totals['users'] / biggest * 100)
        totals['subscriptions_pct'] = int(totals['subscriptions'] / biggest * 100)
        totals['orders_pct'] = int(totals['orders'] / biggest * 100)
        totals['payments_pct'] = int(totals['payments'] / biggest * 100)
    else:
        totals['users_pct'] = 0
        totals['subscriptions_pct'] = 0
        totals['orders_pct'] = 0
        totals['payments_pct'] = 0

    totals['faturamento'] = Order.objects.filter(status__in=[3,4]).aggregate(
        Sum('price'))['price__sum']

    approved = Order.objects.filter(status__in=[3, 4]).count()
    try:
        totals['ticket'] = totals['faturamento'] / approved
    except:
        totals['ticket'] = 0

    totals['em_aberto'] = Order.objects.filter(status__in=[0, 1, 2, 5]).count()

    totals['cancelados'] = Order.objects.filter(status__in=[6, 7]).count()

    return render(request, 'panel/dashboard.html', {
        'qt_users': qt_users,

        'qt_subscriptions': qt_subscriptions,
        'pct_subscriptions': pct_subscriptions,

        'qt_orders': qt_orders,
        'pct_orders': pct_orders,

        'qt_payments': qt_payments,
        'pct_payments': pct_payments,

        'today': today,
        'two_weeks': two_weeks,
        
        'chart_labels': chart_labels,
        'chart_users': chart_users,
        'chart_subscriptions': chart_subscriptions,
        'chart_orders': chart_orders,
        'chart_payments': chart_payments,

        'totals': totals,

        'last_subscriptions': last_subscriptions
    })

