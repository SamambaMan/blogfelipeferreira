# -*- coding: utf-8 -*-
"""Módulo com views para RSS feed"""
from django.contrib.syndication.views import Feed
from django.urls import reverse
from .models import Artigo


class UltimosArtigos(Feed):
    """RSS feed das notícias do site"""
    title = u"Últimos Artigos"
    link = "artigos"
    description = u"Últimos artigos publicados"

    def items(self):
        return Artigo.objects.all().order_by("-DataPublicacao")[:20]

    def item_title(self, item):
        return item.Titulo

    def item_description(self, item):
        from django.template.defaultfilters import safe, truncatewords
        return truncatewords(safe(item.Conteudo), 40)

    def item_link(self, item):
        return reverse('artigo', kwargs={'slugpagina':item.Pagina.Slug,
                                       'slugartigo':item.Slug})
