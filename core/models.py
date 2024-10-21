from django.db import models


class Endereco(models.Model):
    rua = models.CharField(max_length=100)
    bairro = models.CharField(max_length=100)
    numero = models.IntegerField()

    def __str__(self):
        return f'{self.rua} - {self.bairro}'
    

class Trajeto(models.Model):
    endereco_comeco = models.ForeignKey(Endereco, on_delete=models.PROTECT, related_name='endereco_trajeto_start')
    endereco_final = models.ForeignKey(Endereco, on_delete=models.PROTECT, related_name='endereco_trajeto_final')
    distancia = models.FloatField()
    tempo_do_trajeto = models.TimeField()


    def __str__(self):
        return f'{self.endereco_comeco} - {self.endereco_final}'


class Treino(models.Model):
    trajeto = models.ForeignKey(Trajeto, on_delete=models.PROTECT, related_name='trajeto_treino')
    pace_realizado = models.TimeField()
    distancia = models.FloatField()
    data = models.DateTimeField()


    def __str__(self):
        return f'{self.trajeto} - {self.data}'
    

class Corrida(models.Model):
    nome = models.CharField(max_length=100)
    distancia_realizada = models.FloatField()
    posicao = models.IntegerField()
    trajeto = models.ForeignKey(Trajeto, on_delete=models.PROTECT, related_name='trajeto_corrida')
    pace = models.TimeField()
    data = models.DateTimeField()


    def __str__(self):
        return f'{self.nome} - {self.posicao}'
    
