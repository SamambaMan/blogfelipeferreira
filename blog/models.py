# -*- coding: utf-8 -*-
"""Modelo de dados do site"""
from __future__ import unicode_literals

from django.db import models
from tinymce.models import HTMLField
from autoslug import AutoSlugField
from ordered_model.models import OrderedModel
from .managers import PaginaManager, ArtigoManager


class Pagina(OrderedModel):
    """Página, entidade que irá guardar os atributos de cada
    página navegavel do site"""
    Titulo = models.CharField(max_length=100)
    Slug = AutoSlugField(populate_from='Titulo', unique=True)
    NomeMenu = models.CharField(max_length=20)
    MostraMenu = models.BooleanField(default=False)
    ImagemTopo = models.FileField(blank=True, null=True)
    Conteudo = HTMLField(blank=True, null=True)
    RodapePagina = HTMLField(blank=True, null=True)
    RodapeGeral = HTMLField(blank=True, null=True)
    Home = models.BooleanField(default=False)
    objects = PaginaManager()

    class Meta(OrderedModel.Meta):
        pass

    def __str__(self):
        if self:
            return self.Titulo
        return ""

class Artigo(models.Model):
    Pagina = models.ForeignKey('Pagina')
    Titulo = models.CharField(max_length=100)
    DataPublicacao = models.DateField(blank=True, null=True)
    Slug = AutoSlugField(populate_from='Titulo', unique=True)
    ImagemTopo = models.FileField(blank=True, null=True)
    Conteudo = HTMLField(blank=True, null=True)
    Publicado = models.BooleanField(default=False)
    Detalhavel = models.BooleanField(default=True)
    objects = ArtigoManager()

    def save(self, *args, **kwargs):
        from datetime import datetime
        if self.Publicado:
            if self.id:
                conteudoanterior = Artigo.objects.get(id=self.id)
                if not conteudoanterior.Publicado:
                    self.DataPublicacao = datetime.now()
            self.DataPublicacao = datetime.now()

        super(Artigo, self).save(*args, **kwargs)
    
    def __str__(self):
        if self:
            return self.Titulo
        return ""

