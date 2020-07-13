import json
from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from core.forms.user import SignupForm
from core.models import UserProfile, PasswordRecoveryToken, Subscription, Order
from core import sendgrid


AUTH_HOME = '/'


def signup(request):
    if request.user.is_authenticated:
        return redirect(AUTH_HOME)

    form = SignupForm()
    if request.POST:
        form = SignupForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(
                username=form.cleaned_data['email'],
                email=form.cleaned_data['email'],
                password=form.cleaned_data['pass1'],
                first_name=form.cleaned_data['name'],
            )

            if user:
                UserProfile(
                    user=user,
                    ddd=form.cleaned_data['ddd'],
                    phone=form.cleaned_data['phone']
                ).save()

                signin(request, form.cleaned_data['email'],
                    form.cleaned_data['pass1'])
                
                request.session['msg'] = 'Seu cadastro foi efetuado com sucesso!'
                request.session['msg_class'] = 'success'

                return redirect('/concursos')


    return render(request, 'core/signup.html', {
        'title': 'Cadastro',
        'form': form
    })


def signin(request, username=None, password=None):
    if request.user.is_authenticated:
        return redirect(AUTH_HOME)

    error = None
    if not username and request.POST:
        username = request.POST['email']
        password = request.POST['password']

    if username and password:
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect(AUTH_HOME)
        else:
            error = 'Email ou senha inválidos.'

    return render(request, 'core/signin.html', {
        'title': 'Entrar',
        'error': error,
        'email': username
    })


def signout(request):
    logout(request)
    return redirect('/')


def change_password(request):
    if not request.user.is_authenticated:
        return redirect(AUTH_HOME)

    error = None
    success = None

    if request.POST:
        current_pass = request.POST['current_pass']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        if pass1 != pass2:
            error = 'As senhas digitadas não são iguais.'
        else:
            user = authenticate(request, username=request.user.username,
                password=current_pass)
            if user:
                user.set_password(pass1)
                user.save()
                login(request, user)
                success = True

            else:
                error = 'A senha atual está incorreta.'

    res = json.dumps({
        'error': error,
        'success': success
    })

    return HttpResponse(res)


def recover_password(request, token=None):
    success = None
    error = None
    prt = None

    if token:
        token = token.replace('/', '')
        prt = PasswordRecoveryToken.objects.filter(token=token)
        if not prt:
            error = 'Token não encontrado.'

    if request.POST:

        if 'email' in request.POST:
            email = request.POST['email']       
            user = User.objects.filter(email=email)

            if user:

                old_prt = PasswordRecoveryToken.objects.filter(user_id=user[0].id)
                if old_prt:
                    old_prt[0].delete()
                
                prt_token = PasswordRecoveryToken().generate_token(user[0].id)

                msg = 'Você solicitou uma recuperação de senha através do site.'
                msg += '<br><br>Por favor clique no link a seguir para efetuar'
                msg += ' a redefinição da sua senha:<br><br>'
                url = 'http://www.rotafestival.com/recuperar-senha/{token}'.format(
                    token=prt_token
                )
                msg += '<a href="{link}">{link}</a>'.format(link=url)
                sendgrid.send(email, 'Recuperação de senha', msg)

                error = None
                success = ('Um email foi enviado contendo instruções '
                           'para recuperação da senha.')
            else:
                error = 'Email não encontrado.'

        elif 'pass1' in request.POST and prt:
            pass1 = request.POST['pass1']
            pass2 = request.POST['pass2']
            if pass1 != pass2:
                error = 'As senhas digitadas não são iguais.'
            else:
                user = User.objects.filter(pk=prt[0].user_id)
                if user:
                    user[0].set_password(pass1)
                    user[0].save()

                    prt[0].delete()
                    success = 'Sua senha foi redefinida com sucesso!'

    return render(request, 'core/recover_password.html', {
        'title': 'Recuperação de senha',
        'token': prt,
        'success': success,
        'error': error
    })


def profile(request):
    return render(request, 'core/profile.html')


def account(request):
    if not request.user.is_authenticated:
        return redirect(AUTH_HOME)

    up = UserProfile.objects.get(user_id=request.user.id)

    subscriptions = Subscription.objects.filter(user_id=request.user.id)
    for subscription in subscriptions:
        subscription.orders = Order.objects.filter(
            subscription_id=subscription.id)

    orders = Order.objects.filter(user_id=request.user.id)

    return render(request, 'core/account.html', {
        'title': 'Minha conta',
        'up': up,
        'subscriptions': subscriptions,
        'orders': orders
    })


def confirmation(request):
    return render(request, 'core/signup_confirmation.html', {
        'title': 'Cadastro realizado com sucesso!'
    })
