from django.shortcuts import render
from.models import Calendario, Antecedentes

# Create your views here.

def index(request):
    return render(request, 'login/login.html', {})

def mostrarUsuario(request):
    qs_Calendario = Calendario.objects.all()
    return render(request, 'login/Calendario.html', {'vAgenda':qs_Calendario})