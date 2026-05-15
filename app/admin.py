from django.contrib import admin
from .models import Categoria, Episodio, Midia, Temporada

admin.site.register(Categoria)
admin.site.register(Midia)
admin.site.register(Temporada)
admin.site.register(Episodio)
