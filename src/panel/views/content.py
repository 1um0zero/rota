from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, redirect, HttpResponse
from core.models import Page
from panel.utils import make_url


@csrf_exempt
def index(request):

    if request.POST:
        order = request.POST['order'].split(',')
        n = 0
        for page_id in order:
            if page_id:
                pid = int(page_id)
                page = Page.objects.get(pk=pid)
                page.order = n
                page.save()
            n += 1

        return HttpResponse()

    pages = Page.objects.all().order_by('order')
    msg = request.session.get('msg', '')
    request.session['msg'] = ''
    return render(request, 'panel/content/index.html', {
        'pages': pages,
        'msg': msg
    })


def form(request, content_id=None):
    page = None
    
    if content_id:
        page = Page.objects.get(pk=content_id)

    if request.POST:

        content = request.POST['content']

        if page and page.fixed:
            page.content = content

        else:
            title = request.POST['title']
            is_published = int(request.POST.get('is_published', 0))
            display_on_menu = int(request.POST.get('display_on_menu', 0))
            url = make_url(title)

            if page:
                page.title = title
                page.status = is_published
                page.display_on_menu = display_on_menu
                page.content = content
                page.url = url
            else:
                page = Page(
                    title=title,
                    status=is_published,
                    content=content,
                    url=url,
                    display_on_menu=display_on_menu
                )

        page.save()

        request.session['msg'] = 'Página salva com sucesso.'

        return redirect('/painel/conteudo')

    return render(request, 'panel/content/form.html', {
        'id': page.id if page else '',
        'title': page.title if page else '',
        'is_published': page.status == 1 if page else '',
        'display_on_menu': page.display_on_menu == 1 if page else '',
        'content': page.content if page else '',
        'fixed': page.fixed if page else False
    })


def delete(request, content_id):
    page = Page.objects.get(pk=content_id)
    page.delete()
    return redirect('/painel/conteudo')
