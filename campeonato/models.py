from django.db import models


class Campeonato(models.Model):
    nome = models.CharField(max_length=200)
    descricao = models.TextField(blank=True)
    data_inicio = models.DateField()
    data_fim = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.nome


class Time(models.Model):
    nome = models.CharField(max_length=150)
    cidade = models.CharField(max_length=150, blank=True)
    cor_uniforme = models.CharField(max_length=50, blank=True)
    campeonato = models.ForeignKey(Campeonato, on_delete=models.CASCADE, related_name='times')

    def __str__(self):
        return self.nome


class Jogador(models.Model):
    nome = models.CharField(max_length=150)
    numero = models.PositiveIntegerField()
    posicao = models.CharField(max_length=50, blank=True)
    time = models.ForeignKey(Time, on_delete=models.CASCADE, related_name='jogadores')

    def __str__(self):
        return f'{self.nome} ({self.time})'


class Partida(models.Model):
    campeonato = models.ForeignKey(Campeonato, on_delete=models.CASCADE, related_name='partidas')
    time_casa = models.ForeignKey(Time, on_delete=models.CASCADE, related_name='partidas_casa')
    time_visitante = models.ForeignKey(Time, on_delete=models.CASCADE, related_name='partidas_visitante')
    gols_casa = models.PositiveIntegerField(default=0)
    gols_visitante = models.PositiveIntegerField(default=0)
    data_partida = models.DateField()
    rodada = models.CharField(max_length=50, blank=True)

    class Meta:
        constraints = [
            models.CheckConstraint(
                condition=~models.Q(time_casa=models.F('time_visitante')),
                name='time_casa_diferente_visitante',
            )
        ]

    def __str__(self):
        return f'{self.time_casa} {self.gols_casa} x {self.gols_visitante} {self.time_visitante}'
