from django.db import models

class Pessoa(models.Model):
   nome = models.CharField(max_length=100) 
   dataNasc = models.DateField()
   email = models.CharField(max_length=100) 
   paisDesejado = models.CharField(max_length=52)

   def __str__(self):
      return self.nome
