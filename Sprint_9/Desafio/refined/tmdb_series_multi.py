import sys
from pyspark.context import SparkContext
from pyspark.sql.functions import col, avg, sum
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

        # Criar a tabela de fatos
        fact_table_df = df.select(
            col("id").alias("serie_id"),
            col("name").alias("title_id"),
            col("first_air_date").alias("first_air_date"),
            col("popularity").alias("popularity"),
            col("vote_average").alias("vote_average"),
            col("vote_count").alias("vote_count")
        ).groupBy("title_id").agg(
            avg("vote_average").alias("avg_vote_average"),
            sum("vote_count").alias("total_vote_count"),
            avg("popularity").alias("avg_popularity")
        )

        # Criar tabelas de dimensões
        dim_title_df = df.select(
            col("id").alias("title_id"),
            col("original_name").alias("original_title"),
            col("name").alias("principal_title"),
            col("backdrop_path").alias("backdrop_path"),
            col("poster_path").alias("poster_path"),
            col("overview").alias("overview")
        ).dropDuplicates()

        dim_year_df = df.select(
            col("first_air_date").alias("first_air_date")
        ).dropDuplicates()

        dim_genre_df = df.select(
            col("genre_ids").alias("genre_ids")
        ).dropDuplicates()

        dim_language_df = df.select(
            col("original_language").alias("language_id"),
            col("original_language").alias("language")
        ).dropDuplicates()

        # Verificar e tratar valores nulos nas tabelas de fato e dimensões
        if fact_table_df.count() == 0 or fact_table_df.dropna().count() == 0:
            raise ValueError("A tabela de fatos está vazia ou contém apenas valores nulos")
        
        # Escrever os dados no formato Parquet
        fact_table_df.write.mode('overwrite').parquet(fact_output_path)
        dim_title_df.write.mode('overwrite').parquet(dim_output_paths['title'])
        dim_year_df.write.mode('overwrite').parquet(dim_output_paths['year'])
        dim_genre_df.write.mode('overwrite').parquet(dim_output_paths['genre'])
        dim_language_df.write.mode('overwrite').parquet(dim_output_paths['language'])
        
        print(f"Dados escritos com sucesso em {fact_output_path} e dimensões")
        
    except Exception as e:
        print(f"Erro ao processar e salvar dados Parquet: {e}")

# Caminho para os dados de entrada e saída
execution_date = datetime.now().strftime('dt=%Y/%m/%d')

parquet_input_path = "s3://bucketdesafio/trusted_zone/tmdb/series/dt=2024-07-28/"
fact_output_path = "s3://bucketdesafio/refined_zone/tmdb_series/fato_series/"
dim_output_paths = {
    'title': "s3://bucketdesafio/refined_zone/tmdb_series/dim_title/",
    'year': "s3://bucketdesafio/refined_zone/tmdb_series/dim_year/",
    'genre': "s3://bucketdesafio/refined_zone/tmdb_series/dim_genre/",
    'language': "s3://bucketdesafio/refined_zone/tmdb_series/dim_language/"
}

# Processar e salvar dados do Parquet
try:
    process_and_save_multidimensional(parquet_input_path, fact_output_path, dim_output_paths)
except Exception as e:
    print(f"Erro ao processar os dados do Parquet: {e}")

# Encerrar o job do Glue
job.commit()