import re
from django.shortcuts import redirect


def menu(get_response):

    def auth(request):
        response = get_response(request)
        
        if not re.findall('^/painel/', request.path):
            pass

        pages = Page.objects.filter(status=1).order_by('order')
        return render(request, 'core/home.html', {
            'pages': pages
        })

        return response

    return auth
