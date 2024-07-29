import json
import requests
import boto3
from botocore.exceptions import NoCredentialsError
from dotenv import load_dotenv
from datetime import datetime
import os

# Carrega as variáveis de ambiente do arquivo .env
load_dotenv()

# Verifica se as credenciais foram carregadas corretamente
access_key = os.getenv('AWS_ACCESS_KEY_ID')
secret_key = os.getenv('AWS_SECRET_ACCESS_KEY')
session_token = os.getenv('AWS_SESSION_TOKEN')
region = os.getenv('AWS_DEFAULT_REGION')
tmdb_api_key = os.getenv('TMDB_API_KEY')

# Configurações do S3 usando variáveis de ambiente
s3 = boto3.client(
    's3',
    aws_access_key_id=access_key,
    aws_secret_access_key=secret_key,
    aws_session_token=session_token,
    region_name=region
)
bucket_name = 'bucketdesafio'
folder_name = 'raw/TMDB/JSON'

def fetch_tmdb_data(url, params, max_results=100):
    results = []
    page = 1
    while len(results) < max_results:
        params['page'] = page
        response = requests.get(url, params=params)
        response.raise_for_status()
        data = response.json()
        results.extend(data['results'])
        if len(data['results']) == 0 or len(results) >= max_results:
            break
        page += 1
    return results[:max_results]

def lambda_handler(event, context):
    try:
        # Configurações da API do TMDB para filmes
        movie_url = 'https://api.themoviedb.org/3/discover/movie'
        movie_params = {
            'api_key': tmdb_api_key,
            'language': 'en-US',
            'sort_by': 'popularity.desc',
            'with_genres': '28,12',  # Ação e Aventura
            'primary_release_date.gte': f'{datetime.now().year - 10}-01-01',
            'primary_release_date.lte': f'{datetime.now().year}-12-31'
        }

        # Configurações da API do TMDB para séries
        tv_url = 'https://api.themoviedb.org/3/discover/tv'
        tv_params = {
            'api_key': tmdb_api_key,
            'language': 'en-US',
            'sort_by': 'popularity.desc',
            'with_genres': '10759',  # Ação e Aventura
            'first_air_date.gte': f'{datetime.now().year - 10}-01-01',
            'first_air_date.lte': f'{datetime.now().year}-12-31'
        }

        # Obter filmes e séries
        movies = fetch_tmdb_data(movie_url, movie_params)
        tv_shows = fetch_tmdb_data(tv_url, tv_params)

        # Obter a data atual
        current_date = datetime.now()
        year = current_date.strftime('%Y')
        month = current_date.strftime('%m')
        day = current_date.strftime('%d')

        # Carregar filmes no S3
        movie_file_name = 'movies.json'
        movie_file_path = f'{folder_name}/{year}/{month}/{day}/{movie_file_name}'
        s3.put_object(Bucket=bucket_name, Key=movie_file_path, Body=json.dumps(movies))

        # Carregar séries no S3
        tv_file_name = 'tv_shows.json'
        tv_file_path = f'{folder_name}/{year}/{month}/{day}/{tv_file_name}'
        s3.put_object(Bucket=bucket_name, Key=tv_file_path, Body=json.dumps(tv_shows))

        return {
            'statusCode': 200,
            'body': json.dumps('Dados carregados com sucesso!')
        }
    except NoCredentialsError:
        return {
            'statusCode': 403,
            'body': json.dumps('Credenciais da AWS não configuradas corretamente.')
        }
    except requests.exceptions.RequestException as e:
        return {
            'statusCode': 500,
            'body': json.dumps(f'Erro na chamada da API do TMDB: {str(e)}')
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps(f'Erro: {str(e)}')
        }

# Para teste local (fora do AWS Lambda)
if __name__ == "__main__":
    event = {}
    context = {}
    print(lambda_handler(event, context))
