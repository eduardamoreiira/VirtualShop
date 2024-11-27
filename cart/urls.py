from django.contrib import admin
from django.urls import path
from . import views

app_name = 'cart'

urlpatterns = [
    path( '', views.cart_detalhe, name= 'cart_detalhe'),
    path('adicionar/<int:produto_id>/', views.cart_adicionar, name='cart_adicionar'),
    path('remover/<int:produto_id>/', views.cart_remover, name='cart_remover'),
]