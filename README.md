# Músicas mais tocadas no Deezer
Este projeto busca as 10 músicas mais populares atualmente na plataforma Deezer, utilizando Python e o pacote Requests para consumir a API da plataforma.

URL utilizada para requisição dos dados: <br>
https://api.deezer.com/chart/tracks

## Como executar o projeto:

- Clone o repositório <br><br>
- Navegue até o diretório do projeto <br><br>
- Ative o ambiente virtual: <br>
.\ProjetoApi\venv\Scripts>activate.bat <br><br>
- Instale o Pacote Requests: <br>
pip install requests <br><br>
- Gere o arquivo requirements.txt que lista todas as dependências do ambiente virtual Python atual com suas versões: <br>
pip freeze > requirements.txt <br><br>
- Na pasta do projeto inicie o servidor de desenvolvimento Django: <br>
\ProjetoApi\API>python manage.py runserver <br>
<br><br>
Após seguir esses passos, você poderá acessar as músicas mais tocadas consultando a rota específica definida no projeto.

