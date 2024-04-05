from django.shortcuts import HttpResponse
from django.shortcuts import render
import requests

def Charts(request): 
    try:
        url = "https://api.deezer.com/chart/tracks"
        resposta = requests.get(url)

        if resposta.status_code == 200: 
            dados = resposta.json()
            musicas = []

            for track in dados['tracks']['data']:
                musicas.append({
                    # posicao no charts 
                    'position': track['position'],

                    # nome da musica
                    'title': track['title_short'],

                    # nome do artista
                    'artist': track['artist']['name'],

                    # nome do album
                    'album': track['album']['title']
                })    

            return render(request, 'musicas.html', {'musicas': musicas})
        else: 
            return HttpResponse("Erro ao acessar a API", status=resposta.status_code)
    except: 
        return HttpResponse("Erro ao se conectar") 