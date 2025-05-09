from django.db import models

class Cliente(models.Model):
    nome = models.CharField(max_length=20)
    sobrenome = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    contato = models.CharField(max_length=15)
    cpf= models.CharField(max_length=14)
    def __str__(self) -> str:
        return self.nome

class veiculo(models.Model):
    tipo = models.CharField(max_length=50)
    modelo = models.CharField(max_length=50)
    placa = models.CharField(max_length=8)
    ano = models.IntegerField()
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    lavagens = models.IntegerField(default=0)
    concertos = models.IntegerField(default=0)
    def __str__(self) -> str:
        return self.placa
    
