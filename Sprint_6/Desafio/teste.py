import boto3
import pandas as pd
import datetime
from dotenv import load_dotenv
import os

# Carrega as variáveis de ambiente do arquivo .env
load_dotenv()

# Verifica se as credenciais foram carregadas corretamente
access_key = os.getenv('AWS_ACCESS_KEY_ID')
secret_key = os.getenv('AWS_SECRET_ACCESS_KEY')
session_token = os.getenv('AWS_SESSION_TOKEN')
region = os.getenv('AWS_DEFAULT_REGION')

# Imprime as credenciais para verificação
print(f"AWS_ACCESS_KEY_ID: {access_key}")
print(f"AWS_SECRET_ACCESS_KEY: {secret_key}")
print(f"AWS_SESSION_TOKEN: {session_token}")
print(f"AWS_DEFAULT_REGION: {region}")

if not access_key or not secret_key or not region:
    raise Exception("Credenciais da AWS não foram carregadas corretamente do arquivo .env")

# Função para ler arquivos CSV
def ler_csv(caminho):
    try:
        return pd.read_csv(caminho, delimiter='|')
    except pd.errors.ParserError as e:
        print(f"Erro ao ler o arquivo {caminho}: {e}")
        return None

# Defina os caminhos dos arquivos CSV locais
arquivo_csv1 = 'data/movies.csv'
arquivo_csv2 = 'data/series.csv'

# Leia os arquivos CSV
df1 = ler_csv(arquivo_csv1)
df2 = ler_csv(arquivo_csv2)

# Exiba os DataFrames para confirmar que foram lidos corretamente
print("Conteúdo do arquivo movies.csv:")
print(df1)

print("\nConteúdo do arquivo series.csv:")
print(df2)

# Cria um cliente S3 usando boto3.client
if session_token:
    s3_client = boto3.client(
        's3',
        aws_access_key_id=access_key,
        aws_secret_access_key=secret_key,
        aws_session_token=session_token,
        region_name=region
    )
else:
    s3_client = boto3.client(
        's3',
        aws_access_key_id=access_key,
        aws_secret_access_key=secret_key,
        region_name=region
    )

# Nome do bucket
bucket_name = 'bucketdesafio'

# Verifica se o bucket já existe
def bucket_exists(bucket_name):
    try:
        s3_client.head_bucket(Bucket=bucket_name)
        return True
    except:
        return False

# Cria o bucket se ele não existir
if not bucket_exists(bucket_name):
    try:
        s3_client.create_bucket(Bucket=bucket_name, CreateBucketConfiguration={'LocationConstraint': region})
        print(f"Bucket '{bucket_name}' criado com sucesso.")
    except Exception as e:
        print(f"Erro ao criar o bucket {bucket_name}: {e}")
else:
    print(f"Bucket '{bucket_name}' já existe.")

# Função para fazer upload de arquivos CSV para o S3
def fazer_upload_csv(bucket_name, camada, origem, formato, especificacao, arquivo_local):
    data_processamento = datetime.datetime.now().strftime('%Y/%m/%d')
    caminho_s3 = f"{camada}/{origem}/{formato}/{especificacao}/{data_processamento}/{arquivo_local.split('/')[-1]}"
    try:
        s3_client.upload_file(arquivo_local, bucket_name, caminho_s3)
        print(f"Arquivo '{arquivo_local}' enviado para 's3://{bucket_name}/{caminho_s3}' com sucesso.")
    except Exception as e:
        print(f"Erro ao enviar o arquivo '{arquivo_local}': {e}")

# Parâmetros de upload
camada = 'raw'
origem = 'local'
formato = 'csv'
movies = 'Movies'
series = 'Series'

# Fazer upload dos arquivos CSV para o S3
fazer_upload_csv(bucket_name, camada, origem, formato, movies, arquivo_csv1)
fazer_upload_csv(bucket_name, camada, origem, formato, series, arquivo_csv2)
