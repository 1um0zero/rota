import os
import json
import filetype
from uuid import uuid4
from django.shortcuts import render, redirect, HttpResponse
from rota.settings import CONFIG
from core import sendgrid
from core.models import Contest, Subscription, Order, UserProfile
from core.forms.concurso_roteiros import ConcursoRoteiros
from core.forms.mostra import MostraCompetitiva
from core.forms.lab import Lab
from core.forms.encontro import Encontro
from rota.settings import UPLOAD_DIR


def contest(request, url):
    error = None
    success = False
    contest = Contest.objects.get(url=url)
    block_user = False

    forms = {
        1: ConcursoRoteiros,
        2: Encontro,
        3: Lab,
        4: MostraCompetitiva,
        5: MostraCompetitiva, # seminário
    }

    if contest.id not in forms:
        return HttpResponseNotFound('Form not found for this contest.')

    form = forms[contest.id]()

    qtd_subscriptions = Subscription.objects.filter(user_id=request.user.id,
        contest_id=contest.id, status=1).count()

    has_limit = contest.has_limit()

    if contest.is_free and qtd_subscriptions >= 3:
        error = 'Você já enviou 3 inscrições para este concurso.'
        block_user = True

    else:
        if request.POST:
            if not has_limit:
                error = 'Inscrições encerradas.'

            else:
                data = {}
                form = forms[contest.id](request.POST, request.FILES)

                if form.is_valid():

                    for field in request.POST:
                        if field != 'csrfmiddlewaretoken':
                            data[field] = form.cleaned_data.get(field)

                    for filefield in request.FILES:
                        filename = str(uuid4())
                        path = os.path.join(UPLOAD_DIR, filename)

                        with open(path, 'wb') as _f:
                            for chunk in request.FILES[filefield].chunks():
                                _f.write(chunk)
                        
                        ext = str(filetype.guess(path).extension).lower()
                        newpath = path + '.' + ext
                        os.rename(path, newpath)
                        data[filefield] = filename + '.' + ext
                    
                    # Subscription success
                    success = True
                    subscription = Subscription(user_id=request.user.id,
                        contest_id=contest.id, data=json.dumps(data))
                    subscription.save()
                    
                    user_profile = UserProfile.objects.get(user=request.user)

                    msg = """Olá, {name}!<br><br>Sua inscrição para o {concurso} do IV Rota foi recebida.
                        Em breve, entraremos em contato para confirmar se está
                        tudo certo com a sua documentação. É só aguardar um
                        pouquinho, ok?
                    """.format(
                        name=user_profile.get_name(),
                        concurso=contest.name
                    )
                    sendgrid.send(request.user.email, 'Inscrição confirmada', msg)
                    
                    #if CONFIG.get('is_prod'):
                    #    rota_mail = "rotafestival@gmail.com,rafapaz@gmail.com"
                    #    msg = "Inscrição de número {} recebida.".format(subscription.id)
                    #    sendgrid.send(rota_mail, 'Inscrição recebida', msg)
                    #else:
                    #    print('skipping prod mail')

                    if contest.is_free:
                        return redirect('/confirmacao-inscricao')

                    else:
                        request.session['msg'] = 'Sua inscrição foi recebida. Em breve, entraremos em contato para confirmar se está tudo certo com a sua documentação. É só aguardar um pouquinho, ok? '
                        request.session['msg_class'] = 'success'
                        request.session['subscription_id'] = subscription.id
                        request.session['contest_id'] = contest.id
                        request.session.modified = True

                        return redirect('/planos-e-precos')

                else:
                    error = 'Por favor, verifique os erros abaixo.'


    return render(request, 'core/contest.html', {
        'title': contest.name,
        'contest': contest,
        'form': form,
        'error': error,
        'success': success,
        'qtd_subscriptions': qtd_subscriptions,
        'has_limit': has_limit,
        'block_user': block_user,
    })

