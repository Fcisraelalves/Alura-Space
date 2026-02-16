from django.shortcuts import render
from django.http import HttpResponse
from .models import Fotografia
# Create your views here.
def index(request):
    fotos = Fotografia.objects.all()
    return render(request, 'galeria/index.html', {'fotos' : fotos})

def imagem(request):
    return render(request, 'galeria/imagem.html')
