from django.db import models
from django.urls import reverse

# Create your models here.
class Categoria(models.Model):
    nome = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)

    class Meta:
        ordering = ['nome']
        indexes = [
            models.Index(fields=['nome']),
        ]
        verbose_name = 'categoria'
        verbose_name_plural = 'categorias'

    def __str__(self):
        return self.nome
    
    class Categoria(models.Model):
        def get_absolute_url(self):
            return reverse(
                'shop:produto_list_por_categoria', args=[self.slug]
            )

class Produto(models.Model):
    categoria = models.ForeignKey(
        Categoria,
        related_name='produtos',
        on_delete=models.CASCADE
    )
    nome=models.CharField(max_length=200)
    slug=models.SlugField(max_length=200)
    imagem=models.ImageField(
        upload_to='produtos/%Y/%m/$d',
        blank=True
    )
    descricao=models.TextField(blank=True)
    preco=models.DecimalField(max_digits=10, decimal_places=2)
    disponivel=models.BooleanField(default=True)
    criado=models.DateTimeField(auto_now_add=True)
    atualizado=models.DateTimeField(auto_now=True)

    class Meta:
        ordering=['nome']
        indexes=[
            models.Index(fields=['id','slug']),
            models.Index(fields=['nome']),
            models.Index(fields=['-criado']),
        ]

    def __str__(self):
        return self.nome
    
    class Produto(models.Model):
        def get_absolute_url(self):
            return reverse(
                'shop:produto_detalhe', args=[self.id, self.slug]
            )


