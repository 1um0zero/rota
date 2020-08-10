import re
from django import template
from django.utils.html import mark_safe

register = template.Library()

def real(number):
    _num = str(number).split('.')
    int_real = thousands(_num[0])
    num = 'R$ ' + int_real + ','
    if len(_num) > 1:
        if len(_num[1]) == 1:
            num += (_num[1] + '0')
        else:
            num += _num[1][:2]
    else:
        num += '00'

    return num

register.filter('real', real)

def thousands(num):
    try:
        num = int(num)
    except:
        num = 0
        
    if num >= 1000:
        _n = str(num / 1000).split('.')
        res = _n[0] + '.'
        while len(_n[1]) < 3:
            _n[1] += '0'
        num = res + _n[1]
    return str(num)


def real_float(price):
    return str(price).replace(',', '.')
register.filter('realFloat', real_float)


def youtube(url):
    url = url.replace('/watch?v=', '/embed/')
    if 'youtube' not in url and 'youtu.be' not in url:
        url = 'about:blank'
    return url
register.filter('youtube', youtube)


def vimeo(url):
    res = re.findall(r'vimeo.com/([0-9]*)', url)
    if res:
        return 'https://player.vimeo.com/video/' + res[0] + '?title=0&byline=0&portrait=0'
    return url    
register.filter('vimeo', vimeo)


def pagseguro_status(status):
    statuses = {
        0: 'Pedido realizado',
        1: 'Aguardando pagamento',
        2: 'Em análise',
        3: 'Pagamento aprovado',
        #4: 'Disponível',
        4: 'Pagamento aprovado',
        5: 'Em disputa',
        6: 'Devolvido',
        7: 'Cancelado',
        8: 'Gratuito',
    }
    return statuses.get(status)

register.filter('pagseguro_status', pagseguro_status)


def pagseguro_method(method):
    if method == 0:
        return 'cartão de crédito'

    return 'pedido realizado'

register.filter('pagseguro_method', pagseguro_method)


def yesno(val):
    if val:
        res =  '<span class="label label-success">sim</span>'
    else:
        res = '<span class="label label-danger">não</span>'

    return mark_safe(res)

register.filter('yesno', yesno)


def is_image(src):
    if src:
        if re.findall('(\.png|\.gif|\.jpe?g)$', src.lower()):
            return True
    return False

register.filter('is_image', is_image)


def _list(content):
    return ', '.join(content)
register.filter('list', _list)


def nl2br(content):
    content = content.replace('<', '&lt;').replace('>', '&gt;')
    return content.replace('\n', '<br>\n')

register.filter('nl2br', nl2br)


def sanitize(content):
    # content = re.sub('style="([^"]+)"', '', content)
    return content

register.filter('sanitize', sanitize)


def uppercase(text):
    return text.upper()
register.filter('uppercase', uppercase)


def is_youtube(url):
    if re.findall(r'(youtube|youtu.be)', url):
        return True
    return False
register.filter('is_youtube', is_youtube)


def is_vimeo(url):
    if re.findall(r'(vimeo)', url):
        return True
    return False
register.filter('is_vimeo', is_vimeo)
