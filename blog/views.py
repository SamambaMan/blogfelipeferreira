# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .models import Pagina, Artigo

# Create your views here.

def index(request):
    menu = Pagina.objects.itensmenu()

    artigos = Artigo.objects.artigos_publicados()

    return render(request, 'blog/index.html', {'menu':menu, 'artigos':artigos})

def pagina(request, slugpagina):

    menu = Pagina.objects.itensmenu()

    paginaatual = Pagina.objects.get(Slug=slugpagina)

    artigos = Artigo.objects.artigos_publicados().filter(Pagina=paginaatual)

    return render(request, 'blog/pagina.html',
                  {'menu':menu,
                   'pagina':paginaatual,
                   'artigos':artigos})


def artigo(request, slugpagina, slugartigo):
    menu = Pagina.objects.itensmenu()

    itemartigo = Artigo.objects.artigos_publicados().get(Pagina__Slug=slugpagina, Slug=slugartigo)

    paginaartigo = Pagina.objects.get(Slug=slugpagina)

    return render(request, 'blog/artigo.html',
                  {'menu':menu,
                   'artigo':itemartigo,
                   'rodapepagina':paginaartigo.RodapePagina})

    