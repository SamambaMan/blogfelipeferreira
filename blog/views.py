# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.

def artigos_publicados():
    from .models import Artigo
    return Artigo.objects.filter(Publicado=True).order_by('-DataPublicacao')

def itensmenu():
    from .models import Pagina
    return Pagina.objects.filter(MostraMenu=True)

def index(request):

    menu = itensmenu()

    artigos = artigos_publicados()

    return render(request, 'blog/index.html', {'menu':menu, 'artigos':artigos})

def pagina(request, slugpagina):
    from .models import Pagina

    menu = itensmenu()

    paginaatual = Pagina.objects.get(Slug=slugpagina)

    artigos = artigos_publicados().filter(Pagina=paginaatual)

    return render(request, 'blog/pagina.html',
                  {'menu':menu,
                   'pagina':paginaatual,
                   'artigos':artigos})


def artigo(request, slugpagina, slugartigo):

    menu = itensmenu()

    itemartigo = artigos_publicados().get(Pagina__Slug=slugpagina, Slug=slugartigo)

    return render(request, 'blog/artigo.html',
                  {'menu':menu,
                   'artigo':itemartigo})

def teste(request):
    print request.body

    return True
    