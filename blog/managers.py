from djano.db import models


class PaginaManager(models.Manager):
    @staticmethod
    def itensmenu():
        from .models import Pagina
        return Pagina.objects.filter(MostraMenu=True).order_by('order')


class ArtigoManager(models.Manager):
    @staticmethod
    def artigos_publicados():
        from .models import Artigo
        return Artigo.objects.filter(Publicado=True).order_by('-DataPublicacao')

