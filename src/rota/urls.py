"""rota URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path, include
from panel import urls as panel_urls
from core.views import pages, user, billing, contest

urlpatterns = [
    #path('admin/', admin.site.urls),
    path('painel/', include(panel_urls)),

    path('', pages.home),
    path('cadastro', user.signup),
    path('entrar', user.signin),
    path('sair', user.signout),
    re_path('recuperar-senha(/\w+)?$', user.recover_password),
    path('conta', user.account),
    path('alterar-senha', user.change_password),

    path('concursos', pages.contests),
    path('concurso/<str:url>', contest.contest),

    path('pagina/<str:url>', pages.content),
    path('pagina/<str:url>', pages.content),

    #path('curtas', pages.shorts),
    #path('roteiros', pages.scripts),
    path('convidados', pages.convidados),

    path('planos-e-precos', billing.index),
    path('gerar-pagamento/<int:subscription_id>', billing.create_payment),
    path('notificacao', billing.notification),

    path('confirmacao-cadastro', user.confirmation),
    path('confirmacao-inscricao', pages.subscription_confirmation),
    path('confirmacao-pagamento', billing.confirmation),

    path('votar', contest.votar),

]
