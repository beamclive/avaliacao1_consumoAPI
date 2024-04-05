from django.shortcuts import HttpResponse
import requests

def MusicasArtistas(): 
    try:
        url = "https://api.deezer.com/chart/tracks"
        resposta = requests.get(url)

        if resposta.status_code == 200: 
            dados = resposta.json()

            for track in dados['tracks']['data']:
                # posicao no charts 
                music_position = track['position']

                # nome da musica
                music_title = track['title_short']

                # nome do artista
                artist_name = track['artist']['name']

                # nome do album
                album_title = track['album']['title']

                print(f"Posição: {music_position}")
                print(f"Nome da música: {music_title}")
                print(f"Artista: {artist_name}")
                print(f"Álbum: {album_title}")
                print()
        else: 
            return HttpResponse("Erro ao acessar a API", status=resposta.status_code)
    except: return HttpResponse("Erro ao se conectar")

MusicasArtistas()