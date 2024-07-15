import sys
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from awsglue.job import Job
from pyspark.sql.functions import col
from datetime import datetime

# Inicializar contexto do Glue
args = getResolvedOptions(sys.argv, ['JOB_NAME'])
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

# Função para processar e salvar os dados
def process_and_save_data(input_path, output_path):
    df = spark.read.csv(input_path, header=True, inferSchema=True, sep='|')
    df.show(5)  # Mostrar as primeiras 5 linhas do dataframe lido

    # Filtrar registros com os gêneros "Aventura" E "Ação" no mesmo campo
    filtered_df = df.filter(col("genero").contains("Adventure") & col("genero").contains("Action"))
    filtered_df.show(5)  # Mostrar as primeiras 5 linhas do dataframe filtrado

    # Verificar e tratar valores nulos
    if filtered_df.count() == 0 or filtered_df.dropna().count() == 0:
        raise ValueError("O DataFrame filtrado está vazio ou contém apenas valores nulos")

    # Escrever os dados no formato Parquet particionando por data de execução
    filtered_df.write.parquet(output_path, mode='overwrite')
    print(f"Dados escritos com sucesso em {output_path}")

# Caminho para os dados de entrada e saída
execution_date = datetime.now().strftime('dt=%Y\%m\%d')

movies_input_path = "s3://bucketdesafio/raw/local/csv/Movies/2024/06/17/"
movies_output_path = f"s3://bucketdesafio/trusted_zone/movies/{execution_date}/"

series_input_path = "s3://bucketdesafio/raw/local/csv/Series/2024/06/17/series.csv"
series_output_path = f"s3://bucketdesafio/trusted_zone/series/{execution_date}/"

# Processar e salvar dados de filmes
try:
    process_and_save_data(movies_input_path, movies_output_path)
except Exception as e:
    print(f"Erro ao processar os dados de filmes: {e}")

# Processar e salvar dados de séries
try:
    process_and_save_data(series_input_path, series_output_path)
except Exception as e:
    print(f"Erro ao processar os dados de séries: {e}")

# Encerrar o job do Glue
job.commit()
