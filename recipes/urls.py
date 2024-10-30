from django.urls import path
from . import views


#HTTP REQUEST <- HTTP RESPONSE (cliente pede e servidor responde)



urlpatterns = [
    path('', views.home_view),
   
    
  
   
]
