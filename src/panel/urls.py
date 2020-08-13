from django.urls import path
from panel.views import (dashboard, content, contests, shorts, scripts,
    acessos, inscricoes, cadastros, orders, projects, encontro, convidados, ranking)


urlpatterns = [
    path('login', dashboard.admin_login),
    path('logout', dashboard.admin_logout),
    path('', dashboard.index),
    path('linhas', contests.index),
    path('linhas/edit/<int:contest_id>', contests.form),
    path('cadastros', cadastros.index),
    path('cadastro/<int:user_id>', cadastros.user),
    path('inscricoes', inscricoes.index),
    path('inscricoes/change_status', inscricoes.change_status),
    path('pedidos', orders.index),
    path('pedido/<int:order_id>', orders.order),
    path('conteudo', content.index),
    path('conteudo/form', content.form),
    path('conteudo/edit/<int:content_id>', content.form),
    path('conteudo/del/<int:content_id>', content.delete),
    path('curtas', shorts.index),
    path('convidados', convidados.index),
    path('convidados/add', convidados.form),
    path('convidados/edit/<int:convidado_id>', convidados.form),
    path('convidados/del/<int:convidado_id>', convidados.delete),
    path('roteiros', scripts.index),
    path('roteiros/download/<int:script_id>', scripts.download),
    path('projetos', projects.index),
    path('projetos/ver/<int:project_id>', projects.view),
    path('encontro', encontro.index),
    path('encontro/ver/<int:project_id>', encontro.view),
    path('folders', encontro.folders),
    path('acessos', acessos.index),
    path('acessos/add', acessos.add),
    path('acessos/del/<int:ur_id>', acessos.remove),
    path('acessos/search', acessos.search),
    path('ranking', ranking.index),
    path('ficha/<int:sub_id>', ranking.ficha),
    path('ranking/promover', ranking.promover),
]

