from django.shortcuts import render
from .models import Nota

def mostrarNotas(request):
    notas = Nota.objects.all()
    print(notas)
    return render(request=request, template_name='mostrar_notas.html', context={'notas': notas})

# Create your views here.
