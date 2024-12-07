from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    genero = models.CharField(
        max_length=20, null=True, 
        choices=(('M', 'Masculino'), ('F', 'Feminino'), ('O', 'Outros' )))
    
    nascimento = models.DateField(null=True, blank=True)

    redesocial = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.username