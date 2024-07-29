import sys
from pyspark.context import SparkContext
from pyspark.sql.functions import col
from awsglue.context import GlueContext
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from awsglue.job import Job
from datetime import datetime

# Inicializar contexto do Glue
args = getResolvedOptions(sys.argv, ['JOB_NAME'])
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

# Função para processar e salvar dados Parquet
def process_and_save_multidimensional(input_path, fact_output_path, dim_output_paths):
    try:
        df = spark.read.parquet(input_path)
        df.show(5)  # Mostrar as primeiras 5 linhas do dataframe lido

        # Selecionar as primeiras 5 linhas
        top5_df = df.limit(5)
        top5_df.show()  # Mostrar as 5 linhas selecionadas

        # Criar a tabela de fatos
        fact_table_df = df.select(
            col("id").alias("movie_id"),
            col("titulopincipal").alias("title_id"),
            col("anolancamento").alias("year_id"),
            col("genero").alias("genre_id")
        )
        
        # Criar tabelas de dimensões
        dim_title_df = df.select(
            col("id").alias("title_id"),
            col("titulooriginal").alias("original_title"),
            col("titulopincipal").alias("principal_title")
        ).dropDuplicates()

        dim_year_df = df.select(
            col("anolancamento").alias("year_id"),
            col("anolancamento").alias("release_year")
        ).dropDuplicates()

        dim_genre_df = df.select(
            col("genero").alias("genre_id"),
            col("genero").alias("genre")
        ).dropDuplicates()

        dim_artist_df = df.select(
            col("nomeartista").alias("artist_name"),
            col("profissao").alias("profession"),
            col("personagem").alias("character")
        ).dropDuplicates()

        # Verificar e tratar valores nulos nas tabelas de fato e dimensões
        if fact_table_df.count() == 0 or fact_table_df.dropna().count() == 0:
            raise ValueError("A tabela de fatos está vazia ou contém apenas valores nulos")
        
        # Escrever os dados no formato Parquet
        fact_table_df.write.parquet(fact_output_path, mode='overwrite')
        dim_title_df.write.parquet(dim_output_paths['title'], mode='overwrite')
        dim_year_df.write.parquet(dim_output_paths['year'], mode='overwrite')
        dim_genre_df.write.parquet(dim_output_paths['genre'], mode='overwrite')
        dim_artist_df.write.parquet(dim_output_paths['artist'], mode='overwrite')
        
        print(f"Dados escritos com sucesso em {fact_output_path} e dimensões")
        
    except Exception as e:
        print(f"Erro ao processar e salvar dados Parquet: {e}")

# Caminho para os dados de entrada e saída
execution_date = datetime.now().strftime('dt=%Y/%m/%d')

parquet_input_path = "s3://bucketdesafio/trusted_zone/movies/dt=2024-07-28/"
fact_output_path = "s3://bucketdesafio/refined_zone/movies/fato_movies/"
dim_output_paths = {
    'title': "s3://bucketdesafio/refined_zone/movies/dim_title/",
    'year': "s3://bucketdesafio/refined_zone/movies/dim_year/",
    'genre': "s3://bucketdesafio/refined_zone/movies/dim_genre/",
    'artist': "s3://bucketdesafio/refined_zone/movies/dim_artist/"
}

# Processar e salvar dados do Parquet
try:
    process_and_save_multidimensional(parquet_input_path, fact_output_path, dim_output_paths)
except Exception as e:
    print(f"Erro ao processar os dados do Parquet: {e}")

# Encerrar o job do Glue
job.commit()