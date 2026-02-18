from django.db import models
from datetime import datetime

# Create your models here.
class Categorias(models.TextChoices):
    GALAXIA = 'GALAXIA', 'Galáxia'
    ESTRELA = 'ESTRELA', 'Estrela'
    PLANETA = 'PLANETA', 'Planeta'
    NEBULOSA = 'NEBULOSA', 'Nebulosa'
    LUA = 'LUA', 'Lua'

class Fotografia(models.Model):
    nome = models.CharField(max_length=100, null=False, blank=False)
    categoria = models.CharField(max_length=100, choices=Categorias.choices, default=Categorias.GALAXIA)
    legenda = models.CharField(max_length=150, null=False, blank=False)
    descricao = models.TextField(null=False, blank=False)
    foto = models.ImageField(upload_to='fotos/%Y/%m/%d/', blank=True)
    publicada = models.BooleanField(default=False)
    data_fotografia = models.DateTimeField(default=datetime.now, blank=False)

    def __str__(self):
        return f'Fotografia [nome={self.nome}]'
    
