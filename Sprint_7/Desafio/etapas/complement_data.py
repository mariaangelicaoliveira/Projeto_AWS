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

def lambda_handler(event, context):
    try:
        # Configurações da API do TMDB
        tmdb_url = 'https://api.themoviedb.org/3/movie/popular'
        params = {'api_key': tmdb_api_key, 'language': 'en-US', 'page': 1}

        # Chamada à API do TMDB
        response = requests.get(tmdb_url, params=params)
        response.raise_for_status()  # Levanta um erro para códigos de status ruins
        data = response.json()

        # Obter a data atual
        current_date = datetime.now()
        year = current_date.strftime('%Y')
        month = current_date.strftime('%m')
        day = current_date.strftime('%d')

        # Agrupar dados em lotes de 100 registros
        batches = [data['results'][i:i + 100] for i in range(0, len(data['results']), 100)]

        for i, batch in enumerate(batches):
            file_name = f'movies_batch_{i}.json'
            file_path = f'{folder_name}/{year}/{month}/{day}/{file_name}'
            s3.put_object(Bucket=bucket_name, Key=file_path, Body=json.dumps(batch))

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
