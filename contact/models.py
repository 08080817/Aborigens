from django.db import models
from django.utils import timezone

# Create your models here.
class Contato(models.Model):
    nome = models.CharField(max_length=26)
    sobrenome = models.CharField(max_length=50)
    email = models.EmailField() #Volta pra view
    telefone = models.IntegerField() #e o (55) 11 - ? NO PLACEHOLDER
    celular = models.IntegerField() #e o (55) 11 - ? NO PLACEHOLDER
    site = models.URLField()

    # def __str__(self):
    #      return self.nome, self.sobrenome

class Mensagem(models.Model):
    data = models.DateTimeField(default=timezone.now)
    texto = models.CharField(max_length=1000)
    # usuario = models.OneToMany(Usuario, blank=False)
    contato = models.ForeignKey(Contato, on_delete=models.CASCADE)