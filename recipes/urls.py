from django.contrib import admin
from django.http import HttpResponse
from django.urls import path
from recipes.views import contato_view, sobre_view, home_view


#HTTP REQUEST <- HTTP RESPONSE (cliente pede e servidor responde)



urlpatterns = [
    path('', home_view),
    path('admin/', admin.site.urls),
    path('sobre/', sobre_view),
    path('contato/', contato_view)
]
