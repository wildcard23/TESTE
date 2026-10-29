from django.shortcuts import render


def home(request):
    times = [
        {'nome': 'Tigres', 'pontos': 12, 'j': 5, 'v': 4, 'e': 0, 'd': 1, 'gp': 15, 'gc': 7},
        {'nome': 'Leões', 'pontos': 11, 'j': 5, 'v': 3, 'e': 2, 'd': 0, 'gp': 13, 'gc': 8},
        {'nome': 'Dragões', 'pontos': 10, 'j': 5, 'v': 3, 'e': 1, 'd': 1, 'gp': 12, 'gc': 9},
        {'nome': 'Falcões', 'pontos': 8, 'j': 5, 'v': 2, 'e': 2, 'd': 1, 'gp': 10, 'gc': 9},
        {'nome': 'Vikings', 'pontos': 6, 'j': 5, 'v': 2, 'e': 0, 'd': 3, 'gp': 9, 'gc': 12},
        {'nome': 'Cães do Campo', 'pontos': 3, 'j': 5, 'v': 1, 'e': 0, 'd': 4, 'gp': 7, 'gc': 17},
    ]

    partidas = [
        'Tigres 3 x 1 Falcões',
        'Leões 2 x 2 Dragões',
        'Vikings 1 x 0 Cães do Campo',
        'Dragões 4 x 2 Vikings',
    ]

    contexto = {
        'titulo': 'Campeonato de Futsal',
        'rodada': 5,
        'times': times,
        'partidas': partidas,
    }
    return render(request, 'campeonato/home.html', contexto)
