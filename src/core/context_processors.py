from core.models import Contest, Page
from rota.settings import CONFIG


def default(request):
    menu = [
        # {'title': 'Home', 'url': '/'},
        # {'title': 'Concursos', 'url': '/concursos'}
    ]

    pages = Page.objects.filter(
        status=True,
        display_on_menu=True
    ).order_by('order')

    for page in pages:
        url = '/pagina/' + page.url
        if page.title == 'Home' and page.fixed:
            url = '/'

        menu.append({
            'title': page.title,
            'url': url
        })

    contests = Contest.objects.filter(display_on_site=True).order_by('name')
    for contest in contests:
        menu.append({
            'title': contest.name,
            'url': '/concurso/' + contest.url
        })

    menu.append({
        'title': 'Planos e preços',
        'url': '/planos-e-precos',
    })

    menu.append({
        'title': 'Convidados',
        'url': '/convidados',
    })



    return {
        'current_page': request.path,
        'pages': menu,
        'is_prod': CONFIG.get('is_prod')
    }
