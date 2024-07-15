import sys
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from awsglue.job import Job
from pyspark.sql.functions import col, array_contains
from datetime import datetime

# Inicializar contexto do Glue
args = getResolvedOptions(sys.argv, ['JOB_NAME'])
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

# Função para processar e salvar dados JSON
def process_and_save_json(input_path, output_path):
    df = spark.read.json(input_path)
    df.show(5)  # Mostrar as primeiras 5 linhas do dataframe lido

    # Filtrar registros com os genres_ids contendo 12 (Adventure) e 28 (Action)
    filtered_df = df.filter(array_contains(col("genre_ids"), 12) & array_contains(col("genre_ids"), 28))
    filtered_df.show(5)  # Mostrar as primeiras 5 linhas do dataframe filtrado

    # Verificar e tratar valores nulos
    if filtered_df.count() == 0 or filtered_df.dropna().count() == 0:
        raise ValueError("O DataFrame filtrado está vazio ou contém apenas valores nulos")

    # Escrever os dados no formato Parquet particionando por data de execução
    filtered_df.write.parquet(output_path, mode='overwrite')
    print(f"Dados escritos com sucesso em {output_path}")

# Caminho para os dados de entrada e saída
execution_date = datetime.now().strftime('dt=%Y\%m\%d')

tmdb_json_input_path = "s3://bucketdesafio/raw/TMDB/JSON/2024/06/30/movies_batch_0.json"
tmdb_json_output_path = f"s3://bucketdesafio/trusted_zone/tmdb/{execution_date}/"

# Processar e salvar dados do JSON do TMDB
try:
    process_and_save_json(tmdb_json_input_path, tmdb_json_output_path)
except Exception as e:
    print(f"Erro ao processar os dados do JSON do TMDB: {e}")

# Encerrar o job do Glue
job.commit()
