from django.shortcuts import render, redirect
from core.models import Contest, Subscription
from panel.utils import make_url


def index(request):
    contests = Contest.objects.all()
    for contest in contests:
        contest.subscriptions = Subscription.objects.filter(
            contest_id=contest.id).count()

    msg = request.session.get('msg', '')
    request.session['msg'] = ''
    return render(request, 'panel/contests/index.html', {
        'contests': contests,
        'msg': msg
    })


def form(request, contest_id=None):
    contest = None
    
    if contest_id:
        contest = Contest.objects.get(pk=contest_id)

    if request.POST:
        name = request.POST['name']
        description = request.POST['description']
        regulation = request.POST['regulation']
        limit = int(request.POST['limit'])
        date = request.POST['date']
        image_url = request.POST['image_url']
        display_on_site = int(request.POST['display_on_site'])
        subscription_open = int(request.POST['subscription_open'])
        url = make_url(name)

        if contest:
            contest.name = name
            contest.description = description
            contest.regulation = regulation
            contest.subscription_limit = limit
            contest.url = url
            contest.date = date
            contest.image_url = image_url
            contest.display_on_site = display_on_site
            contest.subscription_open = subscription_open
            contest.save()

        request.session['msg'] = 'Linha de ação salva com sucesso.'

        return redirect('/painel/linhas')

    return render(request, 'panel/contests/form.html', {
        'id': contest.id if contest else '',
        'contest': contest,
    })

