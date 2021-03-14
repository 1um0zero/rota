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
        for id in [3360, 2891, 3846, 2641, 3244, 2478, 2603, 3614, 3724, 3619]:
            sub = Subscription.objects.get(id=id)
            JuriPopular(subscription=sub, category=pitch).save()

        # Mostra Ficção
        for id in [3180, 2282, 2288, 2846, 3508, 2963, 2594]:
            sub = Subscription.objects.get(id=id)
            JuriPopular(subscription=sub, category=ficcao).save()
        
        # Mostra Doc
        for id in [3354, 2363, 2587, 2335, 3895, 3095, 3827, 3867]:
            sub = Subscription.objects.get(id=id)
            JuriPopular(subscription=sub, category=doc).save()
        
    except Exception as error:
        print('Erro inesperado: {}'.format(repr(error)))