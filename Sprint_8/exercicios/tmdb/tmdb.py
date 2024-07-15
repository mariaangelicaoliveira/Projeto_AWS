import requests
import pandas as pd

# Atualize sua chave de API aqui
api_key = "6b17178e0cd4422805c03613163000ea"

url = f"https://api.themoviedb.org/3/movie/top_rated?api_key={api_key}&language=pt-BR"

response = requests.get(url)
data = response.json()

print(data)  # Verifique o conteúdo do JSON retornado

filmes = []

if 'results' in data:
    for movie in data['results']:
        df = {
            'Título': movie['title'],
            'Data de lançamento': movie['release_date'],
            'Visão geral': movie['overview'],
            'Votos': movie['vote_count'],
            'Média de votos': movie['vote_average']
        }
        filmes.append(df)

    df = pd.DataFrame(filmes)
    print(df)
else:
    print("A chave 'results' não está presente na resposta.")
