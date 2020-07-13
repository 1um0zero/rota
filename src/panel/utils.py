import re
import unidecode


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
