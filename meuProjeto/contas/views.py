from django.shortcuts import render

from django.http import HttpResponse
import  datetime

def home(request):
    now = datetime.datetime.now()
   # html ="<html><body>It is Now %s.</body></html>"% now
    return render(request,'contas/home.html')

