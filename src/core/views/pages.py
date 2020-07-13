import os
import re
import json
import filetype
from uuid import uuid4
from django.http import HttpResponseNotFound
from django.shortcuts import render, redirect
from core.models import Contest, Page, Short, Script, Product, Curador
from rota.settings import UPLOAD_DIR


def home(request):
    try:
        page = Page.objects.get(title='Home', fixed=True)
        _products = Product.objects.filter(is_enabled=True)
        products = {}
        for product in _products:
            products[product.slug] = product
    except:
        page = None    
        products = {}

    return render(request, 'core/home.html', {
        'is_home': True,
        'page': page,
        'products': products
    })


def content(request, url):
    page = Page.objects.get(url=url, status=1)
    return render(request, 'core/content.html', {
        'title': page.title,
        'content': page.content
    })


def contests(request):
    error = None
    success = False

    msg = request.session.get('msg', '')
    request.session['msg'] = ''
    msg_class = request.session.get('msg_class', '')
    request.session['msg_class'] = ''

    contests = Contest.objects.filter(display_on_site=1)

    return render(request, 'core/contests.html', {
        'title': 'Linhas de ação do ROTA',
        'contests': contests,
        'msg_class': msg_class,
        'msg': msg
    })


def shorts(request):
    error = None
    success = None

    if 'short_link' in request.POST:
        url = request.POST['short_link']

        if not re.findall('^https?://', url):
            error = 'Por favor envie um link válido.'

        else:
            Short(user_id=request.user.id, url=url).save()
            success = True

    return render(request, 'core/shorts.html', {
        'error': error,
        'success': success
    })


def scripts(request):
    error = None
    success = None
    name = ''

    if 'script' in request.FILES:
        name = request.POST['name']
        script = request.FILES['script']

        filename = str(uuid4()) + '.pdf'
        path = os.path.join(UPLOAD_DIR, filename)

        with open(path, 'wb') as _f:
            for chunk in script.chunks():
                _f.write(chunk)

        if filetype.guess(path).extension == 'pdf':
            Script(user_id=request.user.id,
                   name=name,
                   original_filename=str(script),
                   filename=filename
            ).save()

            success = True

        else:
            os.remove(path)
            error = ('Tipo de arquivo inválido. Somente são aceitos'
                     ' arquivos do tipo PDF.')

    return render(request, 'core/scripts.html', {
        'error': error,
        'success': success,
        'name': name
    })

def subscription_confirmation(request):
    return render(request, 'core/subscription_confirmation.html', {
        'title': 'Sucesso!'
    })


def convidados(request):
    convidados = Curador.objects.all()

    return render(request, 'core/convidados.html', {
        'title': 'Convidados',
        'convidados': convidados
    })
