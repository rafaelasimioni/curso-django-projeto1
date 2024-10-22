from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.



def home_view(request):
    return HttpResponse('Boa noite')


def contato_view(request):
    return HttpResponse('Contato')

def sobre_view(request):
    return HttpResponse('Essa é a página SOBRE ')
    #return HTTP response