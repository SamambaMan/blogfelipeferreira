# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from ordered_model.admin import OrderedModelAdmin

from .models import Pagina, Artigo

class PaginaAdmin(OrderedModelAdmin):
    """ModelAdmin das Páginas"""
    list_display = ('Titulo', 'move_up_down_links')
    ordering = ('order',)

admin.site.register(Pagina, PaginaAdmin)
admin.site.register(Artigo)
