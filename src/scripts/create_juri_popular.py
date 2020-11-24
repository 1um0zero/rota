from django.contrib.auth.models import User
from core.models import UserProfile, Subscription, CategoriaJuriPopular, JuriPopular, Contest, IPJuriPopular
import json

def run(*args):
    try:
        CategoriaJuriPopular.objects.all().delete()
        JuriPopular.objects.all().delete()
        IPJuriPopular.objects.all().delete()

        lab = Contest.objects.get(id=3)
        mostra = Contest.objects.get(id=4)

        pitch = CategoriaJuriPopular(name='Melhor Pitching', contest=lab)
        pitch.save()
        ficcao = CategoriaJuriPopular(name='Melhor Ficção', contest=mostra)
        ficcao.save()
        doc = CategoriaJuriPopular(name='Melhor Documentário', contest=mostra)
        doc.save()

        # Lab
        for id in [1227, 1672, 1674, 1732, 1761, 1762, 1776, 1805, 1811, 1864]:
            sub = Subscription.objects.get(id=id)
            JuriPopular(subscription=sub, category=pitch).save()

        # Mostra Ficção
        for id in [1743,1291,1779,991,1717,1486,1679,1690,1902,1782,1871,1016,1061]:
            sub = Subscription.objects.get(id=id)
            JuriPopular(subscription=sub, category=ficcao).save()
        
        # Mostra Doc
        for id in [1929,1771,1886,1479,1837,1900,1883,1930,1047,1887]:
            sub = Subscription.objects.get(id=id)
            JuriPopular(subscription=sub, category=doc).save()
        
    except Exception as error:
        print('Erro inesperado: {}'.format(repr(error)))