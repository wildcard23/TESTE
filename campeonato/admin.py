from django.contrib import admin
from .models import Campeonato, Time, Jogador, Partida


@admin.register(Campeonato)
class CampeonatoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'data_inicio', 'data_fim')
    search_fields = ('nome',)


@admin.register(Time)
class TimeAdmin(admin.ModelAdmin):
    list_display = ('nome', 'cidade', 'campeonato')
    search_fields = ('nome', 'cidade')
    list_filter = ('campeonato',)


@admin.register(Jogador)
class JogadorAdmin(admin.ModelAdmin):
    list_display = ('nome', 'numero', 'posicao', 'time')
    search_fields = ('nome', 'posicao')
    list_filter = ('time',)


@admin.register(Partida)
class PartidaAdmin(admin.ModelAdmin):
    list_display = ('campeonato', 'time_casa', 'gols_casa', 'gols_visitante', 'time_visitante', 'data_partida')
    list_filter = ('campeonato', 'data_partida')
