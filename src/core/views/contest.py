import os
import json
import filetype
from uuid import uuid4
from django.shortcuts import render, redirect, HttpResponse
from rota.settings import CONFIG
from core import sendgrid
from core.models import Contest, Subscription, Order, UserProfile, CategoriaJuriPopular, JuriPopular, IPJuriPopular, Seminario
from core.forms.concurso_roteiros import ConcursoRoteiros
from core.forms.mostra import MostraCompetitiva
from core.forms.lab import Lab
from core.forms.encontro import Encontro
from core.forms.seminario import Seminario as SeminarioForm
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
        5: SeminarioForm, # seminário
    }

    if contest.id not in forms:
        return HttpResponseNotFound('Form not found for this contest.')

    form = forms[contest.id]()

    qtd_subscriptions = Subscription.objects.filter(user_id=request.user.id,
        contest_id=contest.id, status=1).count()

    has_limit = contest.has_limit()

    categorias = []
    if contest.juri_popular_open:        
        cats = CategoriaJuriPopular.objects.filter(contest_id=contest.id)
        for c in cats:
            categoria = dict()
            categoria['id'] = c.id
            categoria['nome'] = c.name            
            projetos = JuriPopular.objects.filter(category=c).all()
            categoria['projetos'] = []            
            for p in projetos:
                dados = json.loads(p.subscription.data)
                categoria['projetos'].append({'id': p.subscription.id, 'nome': dados['title' if 'title' in dados else 'titulo'], 'url': dados['url'] if 'url' in dados else ''})             
            categorias.append(categoria)

    inscritos_sem = Subscription.objects.filter(contest_id=5).all()
    qtd_sem = dict()
    for i in inscritos_sem:
        data = json.loads(i.data)
        sem_ids = [int(v) for v in data['events'].split(',')]
        for k in sem_ids:
            if k not in qtd_sem:
                qtd_sem[k] = 0
            qtd_sem[k] += 1

    dias_semana = ['Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta', 'Sábado', 'Domingo']
    seminarios = Seminario.objects.order_by('date').all()
    sem_dia = dict()
    for s in seminarios:
        esgotado = False
        dia = '{}/{} - {}'.format(s.date.day, s.date.month, dias_semana[s.date.weekday()])
        if dia not in sem_dia:
            sem_dia[dia] = list()
        if s.id in qtd_sem and qtd_sem[s.id] > (contest.subscription_limit-1):
            esgotado = True
        sem_dia[dia].append({'id': s.id, 'name': s.name, 'description': s.description, 'time': '{}:{}'.format(s.date.hour, s.date.minute), 'esgotado': esgotado})
 

    if contest.id == 2 and qtd_subscriptions >= 6:
        error = 'Você já enviou 6 inscrições para este concurso.'
        block_user = True
    elif contest.id != 2 and contest.is_free and qtd_subscriptions >= 3:
        error = 'Você já enviou 3 inscrições para este concurso.'
        block_user = True
    else:
        if request.POST:            
            if contest.id != 5 and not has_limit:
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
                        try:
                            ext = str(filetype.guess(path).extension).lower()
                        except:
                            ext = str(request.FILES[filefield])[-3:].lower()
                        newpath = path + '.' + ext
                        os.rename(path, newpath)
                        data[filefield] = filename + '.' + ext
                    
                    # Subscription success
                    success = True

                    if contest.id == 5:
                        Subscription.objects.filter(user_id=request.user.id, contest_id=5).delete()

                    subscription = Subscription(user_id=request.user.id,
                        contest_id=contest.id, data=json.dumps(data))
                    subscription.save()
                    
                    user_profile = UserProfile.objects.get(user=request.user)

                    msg = """Olá, {name}!<br><br>Sua inscrição para o {concurso} do V Rota foi aceita com sucesso!                        
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
                        request.session['msg'] = 'Sua inscrição foi aceita com sucesso!'
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
        'categorias': categorias,
        'seminarios': sem_dia
    })


def votar(request):
    try:
        sub_id = request.POST['subscription_id']
        cat_id = request.POST['categoria_id']
        ip = request.POST['ip']

        jp = JuriPopular.objects.get(subscription_id=sub_id, category_id=cat_id)
        if IPJuriPopular.objects.filter(ip=ip, category_id=cat_id).exists():
            raise

        jp.votes += 1
        jp.save()

        IPJuriPopular(ip=ip, category_id=cat_id).save()
        return HttpResponse('OK')
    except:
        return HttpResponse('FAIL')