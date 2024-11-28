from decimal import Decimal
from django.conf import settings
from shop.models import Produto

class Cart:
    def __init__(self, request):
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            #Salva um carrinho vazio na sessão browser
            self.session[settings.CART_SESSION_ID] = {}
            cart = self.session[settings.CART_SESSION_ID]
        self.cart = cart
    
    def add(self, produto, quantidade =1, override_quantidade = False):
        produto_id = str(produto.id)
        if produto.id not in self.cart:
           self.cart[produto_id] = {
               'quantidade' : 0,
               'preco' : str(produto.preco)
           }
        
        if override_quantidade:
            self.cart[produto_id] ['quantidade'] = quantidade
        else:
            self.cart[produto_id] ['quantidade'] += quantidade

        self.save()
    
    def save(self):
        self.session.modified = True
    
    #Iterage com os itens do carrinho para retornar o valor total do carrinho
    def __iter__(self):
        produto_ids = self.cart.keys()
        produtos = Produto.objects.filter(id__in = produto_ids)
        cart = self.cart.copy()
        for produto in produtos:
            cart[str(produto.id)]['produto'] = produto
        for item in cart.values():
            item['preco'] = Decimal(item['preco'])
            item['preco_total'] = item['preco'] * item['quantidade']
            yield item #Faz um retorno da lista de valores para esta funççao

    #retorna o tamanho do carrinho
    def __len__(self):
        return sum(item['quantidade'] for item in self.cart.values())

    #Identifica qual é a sessão e a apaga
    def clear(self):
        del self.session[settings.CART_SESSION_ID]
        self.save()

    #Retorna o preço total do carrinho.     
    def get_preco_total(self):
        return sum(
            Decimal(item['preco']) * item['quantidade']
            for item in self.cart.values()
         )