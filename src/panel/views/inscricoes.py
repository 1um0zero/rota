from django.shortcuts import render, HttpResponse
from core.models import Subscription, Order, UserProfile
from django.views.decorators.csrf import csrf_exempt
from core import sendgrid
from panel.views.acessos import distribute


def index(request):
    
    subscriptions = Subscription.get_table()

    return render(request, 'panel/subscriptions/index.html', {
        'subscriptions': subscriptions
    })


@csrf_exempt
def change_status(request):
    if request.POST:
        subscription = Subscription.objects.get(pk=request.POST.get('id'))

        if int(request.POST.get('status')) == 1:
            qtd_subscriptions = Subscription.objects.filter(user=subscription.user, contest=subscription.contest, status=1).count()
            if subscription.contest.id == 2 and qtd_subscriptions >= 6:
                return HttpResponse('Este usuário já tem seis inscrições para esta linha de ação')
            elif subscription.contest.id != 2 and subscription.contest.is_free and qtd_subscriptions >= 3:
                return HttpResponse('Este usuário já tem três inscrições para esta linha de ação')

        subscription.status = int(request.POST.get('status'))
        subscription.save()
        
        if subscription.status == 0:
            return HttpResponse()
       
        user_profile = UserProfile.objects.get(user=subscription.user)
       
        emails = {
            1: 'rotaconcurso2021@gmail.com',
            2: 'rotaencontro2021@gmail.com',
            3: 'rotalab2021@gmail.com',
            4: 'rotamostra2021@gmail.com',
            5: 'rotaseminario2021@gmail.com'
        }
       
        if subscription.status == 1:               
            msg = """Olá, {name}!<br><br>Sua inscrição de nº {inscricao} está HABILITADA para o {concurso} do V Rota.
                    Fique de olho na lista dos semifinalistas que sairá nas Redes Sociais.<br>
                    Qualquer dúvida entre em contato pelo email {email_concurso}.<br>
                    Boa sorte!
                    """.format(
                        name=user_profile.get_name(),
                        inscricao=subscription.id,
                        concurso=subscription.contest.name,
                        email_concurso=emails[subscription.contest.id]
                    )            
            sendgrid.send(subscription.user.email, 'Inscrição #{} aprovada!'.format(subscription.id), msg)
            distribute(subscription.contest.id)
        elif subscription.status == 2:                    
            msg = """Olá, {name}!<br><br>Sua inscrição para o {concurso} do V Rota foi reprovada.<br>
                    Provavelmente houve algum problema na documentação enviada.<br>
                    Favor entrar em contato pelo email {email_concurso} informando seu número de inscrição #{inscricao}
                    para tentar resolver esta pendência.
                    """.format(
                        name=user_profile.get_name(),
                        concurso=subscription.contest.name,
                        email_concurso=emails[subscription.contest.id],
                        inscricao=subscription.id
                    )            
            sendgrid.send(subscription.user.email, 'Inscrição #{} reprovada!'.format(subscription.id), msg)

    return HttpResponse()
