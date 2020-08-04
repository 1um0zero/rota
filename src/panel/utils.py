import re
import unidecode

ROLE_CURADOR = 1
ROLE_JURADO = 2
ROLE_CABIRIA = 3
ROLE_SINA = 4
ROLE_PLAYER = 5

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
