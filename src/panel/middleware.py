import re
from django.shortcuts import redirect


def auth(get_response):

    def auth(request):
        response = get_response(request)
        
        if re.findall('^/painel/', request.path):

            if not request.session.get('painel'):
                login_url = '/painel/login'
                
                if request.path != login_url:
                    return redirect(login_url)

            else:
                if request.session['painel']['role'][0] > 0: # avaliador
                    urls = [
                        '^/painel/roteiros',
                        '^/painel/projetos',
                        '^/painel/curtas',
                        '^/painel/encontro'
                    ]
                    if request.path != '/painel/':
                        block = True
                        for url in urls:
                            if re.match(url, request.path):
                                block = False
                        if block:
                            return redirect('/painel')

        return response

    return auth
