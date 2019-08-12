from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Transacao
from .form import Trasacaoform
import datetime

def home(request):
    data = {}
    data['now']= datetime.datetime.now()
    data['Transacoes']=['t1','t2','t3']

   # html ="<html><body>It is Now %s.</body></html>"% now
    return render(request,'contas/home.html',data)


def listagem (request):
    data = {}
    data ['Transacoes'] = Transacao.objects.all()
    return render(request,'contas/listagem.html',data)

def nova_Transacao (request):
    data ={}
    form = Trasacaoform(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('url_listagem')
    data ['form']= form
    return render(request,'contas/form.html', data)