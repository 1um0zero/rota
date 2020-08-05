import re
import unidecode
from panel.forms.avaliacao import AvaliacaoConcurso, AvaliacaoConcursoJur, AvaliacaoConcursoCabiria, AvaliacaoLab, AvaliacaoMostra, AvaliacaoMostraJur, AvaliacaoMostraSina

ROTEIRO = 1
ENCONTRO = 2
LABORATORIO = 3
MOSTRA = 4

ROLE_CURADOR = 1
ROLE_JURADO = 2
ROLE_CABIRIA = 3
ROLE_SINA = 4
ROLE_PLAYER = 5

REGRA_AVALIACAO = {
    ROTEIRO: {ROLE_CURADOR: {1: AvaliacaoConcurso}, ROLE_JURADO: {2: AvaliacaoConcursoJur}, ROLE_CABIRIA: {2: AvaliacaoConcursoCabiria} },
    LABORATORIO: {ROLE_CURADOR: {1: AvaliacaoLab, 2: AvaliacaoLab} },
    MOSTRA: {ROLE_CURADOR: {1: AvaliacaoMostra}, ROLE_JURADO: {2: AvaliacaoMostraJur}, ROLE_SINA: {2: AvaliacaoMostraSina} }
}


def ficha_avaliacao(contest_id, role_id, step):
    try:
        return REGRA_AVALIACAO[contest_id][role_id][step]
    except:
        return None


def make_url(title):
    title = title.lower()
    title = unidecode.unidecode(title)
    title = title.replace(' ', '-')
    title = re.sub('([^a-zA-Z0-9-_]+)', '-', title)
    title = re.sub('^-', '', title)
    title = re.sub('-$', '', title)
    while '--' in  title:
        title = title.replace('--', '-')
    return title
