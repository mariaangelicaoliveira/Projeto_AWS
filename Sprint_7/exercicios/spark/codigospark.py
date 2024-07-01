from pyspark.sql import SparkSession

# Inicializar a sessão Spark
spark = SparkSession.builder.appName("WordCount").getOrCreate()

# Ler o arquivo README.md
text_file = spark.read.text("README.md").rdd

# Dividir as linhas em palavras
words = text_file.flatMap(lambda line: line.value.split(" "))

# Contar as palavras
word_counts = words.map(lambda word: (word, 1)).reduceByKey(lambda a, b: a + b)

# Coletar os resultados e exibi-los
for word, count in word_counts.collect():
    print(f"{word}: {count}")

# Parar a sessão Spark
spark.stop()
