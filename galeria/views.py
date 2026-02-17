from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Fotografia
# Create your views here.
def index(request):
    fotos = Fotografia.objects.all()
    return render(request, 'galeria/index.html', {'fotos' : fotos})

def imagem(request, imagem_id):
    #fotografia = Fotografia.objects.filter(id=imagem_id).first() 
    #a abordagem abaixo permite que o Django redirecione automaticamente para uma página 404.
    fotografia = get_object_or_404(Fotografia, id=imagem_id)
    context = {'fotografia' : fotografia}
    return render(request, 'galeria/imagem.html', context)
