from django.db import models


class Corredor(models.Model):
    nome = models.CharField(max_length=100)
    idade = models.IntegerField()
    peso = models.FloatField()
    altura = models.FloatField()

    def __str__(self):
        return self.nome