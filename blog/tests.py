# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.test import TestCase
from .models import Pagina, Artigo


class InclusaoPaginaTest(TestCase):
    def setUp(self):
        Pagina(
            Titulo='NovaPagina',
            NomeMenu='NomeMenuPagina',
            MostraMenu=True,
            Home=False).save()

        Pagina(
            Titulo='NovaPaginaNaoMenu',
            NomeMenu='NomeMenuPaginaNaoMenu',
            MostraMenu=False,
            Home=False).save()

        Pagina(
            Titulo='NovaPaginaNaoMenu',
            NomeMenu='NomeMenuPaginaNaoMenu',
            MostraMenu=False,
            Home=True).save()

    def test_item_menu(self):
        self.assertEqual(
            Pagina.objects.itensmenu().count(),
            1)


class InclusaoArtigoTest(TestCase):
    def setUp(self):
        pagina = Pagina(
            Titulo='PaginaArtigo',
            NomeMenu='PaginaArtigo',
            MostraMenu=False,
            Home=True)

        pagina.save()

        Artigo(
            Pagina=pagina,
            Titulo="TituloArtigo",
            Publicado=True).save()

        Artigo(
            Pagina=pagina,
            Titulo="TituloArtigoNaoPublicado",
            Publicado=False).save()


    def test_obter_artigo_publicado(self):
        self.assertEqual(
            Artigo.objects.artigos_publicados().count(),
            1)
