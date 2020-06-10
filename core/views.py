from django.shortcuts import render, HttpResponse, redirect
from core.models import Evento

# Create your views here.
def eventos(request, titulo_evento):
    return HttpResponse('Local 2: {}'.format(titulo_evento))

#def index(request):
#    return redirect('/agenda/')

def lista_eventos(request):
    usuario_logado = request.user
    #evento = Evento.objects.filter(usuario=usuario_logado)
    evento = Evento.objects.all()
    dados = {'eventos':evento}
    return render(request, 'agenda.html', dados)
