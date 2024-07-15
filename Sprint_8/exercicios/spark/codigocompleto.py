from pyspark.sql import SparkSession
from pyspark.sql.functions import rand, when, expr
import pyspark.sql.functions as F

# Criar a SparkSession
spark = SparkSession.builder \
    .master("local[*]") \
    .appName("Laboratório de Dataframes") \
    .getOrCreate()

# Ler o arquivo 'nomes_aleatorios.txt' como CSV
df_nomes = spark.read.csv("nomes_aleatorios.txt", header=True, inferSchema=True)

# Mostrar as primeiras 5 linhas
df_nomes.show(5)

# Imprimir o schema do DataFrame
df_nomes.printSchema()

# Renomear a coluna 'Frances Bennet' para 'Nomes' (substitua 'Frances Bennet' pelo nome correto se necessário)
df_nomes = df_nomes.withColumnRenamed("Frances Bennet", "Nomes")

# Mostrar as primeiras 10 linhas para confirmar o renomeamento
df_nomes.show(10)

# Adicionar a coluna 'Escolaridade' com valores aleatórios
df_nomes = df_nomes.withColumn("Escolaridade", when(rand() < 0.33, "Fundamental")
                                           .when(rand() < 0.66, "Medio")
                                           .otherwise("Superior"))

# Mostrar as primeiras 10 linhas com a nova coluna 'Escolaridade'
df_nomes.show(10)

# Lista de países da América do Sul
paises = ["Argentina", "Bolívia", "Brasil", "Chile", "Colômbia", "Equador", "Guiana", "Paraguai", "Peru", "Suriname", "Uruguai", "Venezuela", "Guiana Francesa"]

# Criar uma expressão SQL para gerar valores aleatórios a partir da lista de países
expr_str = "array(" + ", ".join([f"'{pais}'" for pais in paises]) + f")[cast(floor(rand() * {len(paises)}) as int)]"

# Adicionar a coluna 'Pais' com valores aleatórios da lista de países
df_nomes = df_nomes.withColumn("Pais", expr(expr_str))

# Mostrar as primeiras 10 linhas com a nova coluna 'Pais'
df_nomes.show(10)

# Adicionar a coluna 'AnoNascimento' com valores aleatórios entre 1945 e 2010
df_nomes = df_nomes.withColumn("AnoNascimento", (F.floor(rand() * (2010 - 1945 + 1)) + 1945).cast("int"))

# Mostrar as primeiras 10 linhas com a nova coluna 'AnoNascimento'
df_nomes.show(10)

# Verificar os nomes das colunas antes de aplicar o filtro e a seleção
print("Colunas do DataFrame:")
print(df_nomes.columns)

# Selecionar pessoas que nasceram a partir do ano 2000
df_select = df_nomes.filter(df_nomes.AnoNascimento >= 2000).select("Nomes")

# Mostrar os primeiros 10 nomes do DataFrame df_select
df_select.show(10)

# Etapa 7: Usando Spark SQL para repetir o processo
# Registrar uma tabela temporária
df_nomes.createOrReplaceTempView("pessoas")

# Usar Spark SQL para selecionar pessoas que nasceram a partir do ano 2000
df_select_sql = spark.sql("SELECT Nomes FROM pessoas WHERE AnoNascimento >= 2000")

# Mostrar os primeiros 10 nomes do DataFrame df_select_sql
df_select_sql.show(10)

# Etapa 8: Contar o número de pessoas da geração Millennials (1980-1994)
df_millennials = df_nomes.filter((df_nomes.AnoNascimento >= 1980) & (df_nomes.AnoNascimento <= 1994))

# Contar o número de pessoas da geração Millennials
num_millennials = df_millennials.count()

print(f"Número de pessoas da geração Millennials: {num_millennials}")

# Etapa 9: Usar Spark SQL para contar o número de pessoas da geração Millennials (1980-1994)
# Registrar uma tabela temporária se ainda não estiver registrada
df_nomes.createOrReplaceTempView("pessoas")

# Usar Spark SQL para contar o número de pessoas da geração Millennials
num_millennials_sql = spark.sql("SELECT COUNT(*) as count FROM pessoas WHERE AnoNascimento >= 1980 AND AnoNascimento <= 1994")

# Mostrar o resultado
num_millennials_sql.show()

# Etapa 10: Usar Spark SQL para obter a quantidade de pessoas de cada país para cada geração
query = """
SELECT
  Pais,
  CASE
    WHEN AnoNascimento BETWEEN 1944 AND 1964 THEN 'Baby Boomers'
    WHEN AnoNascimento BETWEEN 1965 AND 1979 THEN 'Geração X'
    WHEN AnoNascimento BETWEEN 1980 AND 1994 THEN 'Millennials (Geração Y)'
    WHEN AnoNascimento BETWEEN 1995 AND 2015 THEN 'Geração Z'
  END AS Geracao,
  COUNT(*) AS Quantidade
FROM pessoas
GROUP BY Pais, Geracao
ORDER BY Pais, Geracao, Quantidade
"""

# Executar a consulta SQL
df_geracoes = spark.sql(query)

# Mostrar os resultados
df_geracoes.show()
