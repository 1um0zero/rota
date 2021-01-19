from core.models import Folder

def run(*args):
    try:
        
        nivel1 = ['Ficção', 'Não Ficção']
        nivel2 = ['Série', 'Longa', 'Curta']
        nivel3 = ['Ação', 'Aventura', 'Biográfico', 'Comédia', 'Drama',
            'Dramédia', 'Fantasia', 'Híbrido', 'Histórico', 'Infantil', 'Sci-fi', 'Suspense', 'Terror', 'Outros']

        Folder.objects.all().delete()
        
        i = 1
        j = 1000
        k = 2000
        for n1 in nivel1:
            Folder(id=i,name=n1, parent_id=None).save()
            for n2 in nivel2:
                Folder(id=j,name=n2, parent_id=i).save()
                for n3 in nivel3:
                    Folder(id=k,name=n3, parent_id=j).save()
                    k += 1
                j += 1
            i += 1

        
    except Exception as error:
        print('Erro inesperado: {}'.format(repr(error)))