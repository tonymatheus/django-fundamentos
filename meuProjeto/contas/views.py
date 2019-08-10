from django.shortcuts import render
from django.http import HttpResponse
from .models import Transacao
import datetime

def home(request):
    data = {}
    data['now']= datetime.datetime.now()
    data['Transacoes']=['t1','t2','t3']

   # html ="<html><body>It is Now %s.</body></html>"% now
    return render(request,'contas/home.html',data)


def listagem(request):
    data = {}
    data['Transacoes'] = Transacao.objects.all()
    return render(request, 'contas/listagem.html', data)
