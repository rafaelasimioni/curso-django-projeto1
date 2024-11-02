from django.urls import path
from . import views


#HTTP REQUEST <- HTTP RESPONSE (cliente pede e servidor responde)



urlpatterns = [
    path('', views.home_view),
    path('recipes/<int:id>/', views.recipe ) #aqui vai aceitar só número na url, porque o site é de receitas
    
     
]
