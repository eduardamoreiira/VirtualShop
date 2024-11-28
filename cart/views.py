from django.shortcuts import render, get_list_or_404, redirect
from .forms import CartAddQuantityForm
from .cart import Cart
from shop.models import Produto
from django.views.decorators.http import require_POST
from django.shortcuts import get_object_or_404


@require_POST
def cart_adicionar(request, produto_id):
    cart = Cart(request)
    produto = get_object_or_404(Produto, id=produto_id)
    form = CartAddQuantityForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(
            produto=produto, 
            quantidade=cd['quantidade'],
            )
    return redirect('cart:cart_detalhe')

def cart_detalhe (request):
    cart = Cart(request)
    for item in cart:
        item['atualizar_quantidade_form'] = CartAddQuantityForm(
        initial={'quantidade': item['quantidade'], 'override': True}
    )
    return render(request, 'cart/detalhe.html', {'cart': cart})
    
def cart_remover(request, produto_id):
    cart = Cart(request)
    produto = get_list_or_404(Produto, id=produto_id)
    cart.remove(produto)
    return redirect('cart:cart_detalhe')
