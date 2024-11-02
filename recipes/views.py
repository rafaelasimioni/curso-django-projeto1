from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.



def home_view(request):
    return render(request, 'recipes/pages/home.html',context={'name': 'Rafaela Simioni de Ávila'})



def recipe(request,id):
    return render(request, 'recipes/pages/home.html',context={'name': 'Rafaela Simioni de Ávila'})