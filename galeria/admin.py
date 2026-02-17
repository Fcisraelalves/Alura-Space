from django.contrib import admin
from .models import Fotografia
# Register your models here.

class ListandoFotografias(admin.ModelAdmin):
    list_display = ('id', 'nome', 'legenda')
    list_display_links = ['nome']
    search_fields = ['nome']

admin.site.register(Fotografia, ListandoFotografias)