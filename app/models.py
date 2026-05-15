from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _


class TimeStampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)

    class Meta:
        abstract = True


class SoftDeleteModel(models.Model):
    deleted_at = models.DateTimeField(null=True, blank=True)

    def delete(self, using=None, keep_parents=False):
        self.deleted_at = timezone.now()
        self.save()

    class Meta:
        abstract = True


class Categoria(TimeStampedModel):
    nome = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.nome


class Midia(TimeStampedModel):
    class Status(models.IntegerChoices):
        SERIE = 1, _('Série')
        FILME = 2, _('Filme')
    nome = models.CharField(max_length=100, null=False, blank=False)
    descricao = models.CharField(max_length=200, null=True, blank=True)
    data_criacao = models.DateTimeField(null=True)
    categorias = models.ManyToManyField(Categoria)
    tipo = models.SmallIntegerField(choices=Status)

    def __str__(self):
        return self.nome
    

class Temporada(TimeStampedModel):
    ordem = models.IntegerField(null=False)
    nome = models.CharField()
    descricao = models.TextField()
    numero = models.IntegerField()
    midia = models.ForeignKey(Midia, on_delete=models.PROTECT)


class Episodio(TimeStampedModel):
    ordem = models.IntegerField(null=False)
    numero = models.IntegerField()
    titulo = models.CharField()
    descricao = models.TextField()
    duracao = models.IntegerField() # em milisegundos
    temporada = models.ForeignKey(Temporada, on_delete=models.PROTECT)

