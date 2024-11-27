from django.shortcuts import get_object_or_404, render
from .models import Categoria, Produto
from cart.forms import CartAddQuantityForm


def produto_list(request, categoria_slug=None):
    categoria = None
    categorias = Categoria.objects.all()
    produtos = Produto.objects.filter(disponivel=True)
    if categoria_slug:
        categoria = get_object_or_404(Categoria, slug=categoria_slug)
        produtos = produtos.filter(categoria=categoria)
    return render(
        request,
        'shop/produto/list.html',
        {
            'categoria':categoria,
            'categorias':categorias,
            'produtos':produtos
        }
    )

def produto_detalhe(request, id, slug):
    produto = get_object_or_404(
        Produto, id=id, slug=slug, disponivel=True
    )

    cart_produto_form = CartAddQuantityForm
    return render(
        request,
        'shop/produto/detail.html',
        {
            'produto':produto, 'cart_produto_form':cart_produto_form
        }
    )
