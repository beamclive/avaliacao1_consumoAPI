from django.shortcuts import HttpResponse
import requests

def MusicasArtistas(request): 
    url = "https://api.deezer.com/chart"
    resposta = requests.get(url)

    if resposta.status_code == 200: 
        return HttpResponse(resposta.content, content_type="application/json")
    else: 
        return HttpResponse("Erro ao acessar a API", status=resposta.status_code)
