from django.db import models

# Create your models here.
class Colaborador(models.Model):
    nomecolaborador = models.CharField(max_length=50)
    cpf = models.CharField(max_length=11)
    tipo_acesso = models.CharField(max_length=50)
    equipe = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.nome

class Lider(models.Model):
    nomelider = models.CharField(max_length=50)
    cpf = models.CharField(max_length=11)
    tipo_acesso = models.CharField(max_length=50)
    equipe = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.nomelider

class Admin(models.Model):
    nomeadmin = models.CharField(max_length=50)
    cpf = models.CharField(max_length=11)
    tipo_acesso = models.CharField(max_length=50)
    
    def __str__(self) -> str:
        return self.nomeadmin