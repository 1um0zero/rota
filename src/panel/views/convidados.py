import os
import json
import filetype
from uuid import uuid4
from django import forms
from django.shortcuts import render, redirect
from rota.settings import CONVIDADOS_DIR
from core.models import Curador, Contest
from panel.forms.convidados import CuradorForm

def index(request):
    convidados = Curador.objects.all()

    return render(request, 'panel/convidados/index.html', {
        'convidados': convidados
    })

def form(request, convidado_id=None):

    _form = CuradorForm()
    convidado = None

    if convidado_id:
        convidado = Curador.objects.get(pk=convidado_id)
        _form = CuradorForm(instance=convidado)
    else:
        convidado = Curador()
    
    if request.POST:
        _form = CuradorForm(request.POST, request.FILES, instance=convidado)
        
        if _form.is_valid():
            convidado = _form.save(commit=False)
            
            if 'file_picture' in request.FILES:
                if convidado.picture:
                    current_pic = os.path.join(CONVIDADOS_DIR, convidado.picture)
                    os.remove(current_pic)

                filename = str(uuid4())
                path = os.path.join(CONVIDADOS_DIR, filename)
                with open(path, 'wb') as _f:
                    for chunk in request.FILES['file_picture'].chunks():
                        _f.write(chunk)
                
                ext = str(filetype.guess(path).extension).lower()
                newpath = path + '.' + ext
                os.rename(path, newpath)
                convidado.picture = filename + '.' + ext
            
            convidado.save()
            return redirect('/painel/convidados')
        
    return render(request, 'panel/convidados/form.html', {
        'form': _form,
        'convidado': convidado
    })

def delete(request, convidado_id):
    if convidado_id:
        convidado = Curador.objects.get(pk=convidado_id)
        if convidado.picture:
            current_pic = os.path.join(CONVIDADOS_DIR, convidado.picture)

            if os.path.isfile(current_pic):
                os.remove(current_pic)

        convidado.delete()
    return redirect('/painel/convidados')


