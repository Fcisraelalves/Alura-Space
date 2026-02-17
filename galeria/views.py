from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Fotografia
# Create your views here.
def index(request):
    fotos = Fotografia.objects.order_by('-data_fotografia').filter(publicada=True)
    return render(request, 'galeria/index.html', {'fotos' : fotos})

def imagem(request, imagem_id):
    #fotografia = Fotografia.objects.filter(id=imagem_id).first() 
    #a abordagem abaixo permite que o Django redirecione automaticamente para uma página 404.
    fotografia = get_object_or_404(Fotografia, id=imagem_id)
    context = {'fotografia' : fotografia}
    return render(request, 'galeria/imagem.html', context)

def buscar(request):
    fotos = Fotografia.objects.order_by('-data_fotografia').filter(publicada=True)

    if 'buscar' in request.GET:
        nome_a_buscar = request.GET['buscar']
        if nome_a_buscar:
            fotos = fotos.filter(nome__icontains=nome_a_buscar)
    return render(request, 'galeria/buscar.html', {'fotos' : fotos})

def buscar_categoria(request, categoria):
    fotos = Fotografia.objects.order_by('-data_fotografia').filter(publicada=True).filter(categoria=categoria)
    return render(request, 'galeria/buscar.html', {'fotos' : fotos})

