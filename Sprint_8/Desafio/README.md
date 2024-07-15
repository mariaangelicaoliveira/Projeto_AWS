# Desafio

### Arquivos  
1. [Arquivo Python Job 1 - csv series e movies](../Desafio/job_series_movies.py)
2. [Arquivo Python Job 2 - json tmdb](../Desafio/job_tmdb.py)


## 1. AWS Glue

### Usei o AWS Glue Studio para criar e gerenciar tarefas de ETL, dos jobs "moviesAndSeries" e "jsonTMDB".
 
![1](../evidencias/desafio/1.png)

## 2. Código comentado do Job "moviesAndSeries"

### Importações para configur o ambiente para um script ETL no AWS Glue, integrando Spark e funcionalidades específicas do Glue para realizar transformações de dados.
 
![1](../evidencias/desafio/job1_SM/1.png)

### Este trecho configura o ambiente necessário para um job ETL, incluindo a inicialização dos contextos do Spark e do Glue, e a preparação do job para execução.

![1](../evidencias/desafio/job1_SM/2.png)

### Este trecho de código define uma função que lê dados de um arquivo CSV, filtra registros com gêneros Action/Adventure, verifica se há valores nulos e salva os dados filtrados no formato Parquet.

![1](../evidencias/desafio/job1_SM/3.png)

### Este trecho define uma variável execution_date que contém a data atual formatada, que pode ser utilizada para criar diretórios ou caminhos de arquivos baseados na data, ajudando a organizar os dados de entrada e saída por data de execução.

![1](../evidencias/desafio/job1_SM/4.png)

### Este trecho configura os caminhos de entrada e saída para os dados de filmes e séries, armazenando-os em um bucket S3 e organizando os dados processados em diretórios com base na data de execução.

![1](../evidencias/desafio/job1_SM/5.png)

### Este trecho tenta processar e salvar os dados de filmes e séries, exibindo mensagens de erro específicas se ocorrer algum problema durante o processamento.

![1](../evidencias/desafio/job1_SM/6.png)

### Este trecho de código assegura que o job do AWS Glue seja devidamente encerrado, permitindo que o status do job seja atualizado e registrado no console do AWS Glue.

![1](../evidencias/desafio/job1_SM/7.png)

### 3. Execuções do job

![1](../evidencias/desafio/job1_SM/8.png)

### Arquivos Parquet gerados pelo job "moviesAndSeries" do AWS Glue e salvos no bucket S3 na pasta correspondente à data de execução. Cada arquivo representa uma parte dos dados processados. 

### "movies"
![1](../evidencias/desafio/job1_SM/9.png)

### "series"

![1](../evidencias/desafio/job1_SM/10.png)

## 4. Athena - job "moviesAndSeries"

### Consulta dos dados "movies" armazenados no Amazon S3 usando SQL 

![1](../evidencias/desafio/athena_SM/1.png)

### Resultado da consulta 

![1](../evidencias/desafio/athena_SM/2.png)

### Consulta dos dados "series" armazenados no Amazon S3 usando SQL 

![1](../evidencias/desafio/athena_SM/3.png)

### Resultado da consulta 

![1](../evidencias/desafio/athena_SM/4.png)


## 5. Código comentado do Job "moviesAndSeries"
 
### Configurações de ambiente para executar um job ETL, integrando funcionalidades do Spark e do Glue para realizar transformações de dados e gerenciamento de jobs.

![1](../evidencias/desafio/job2_tmdb/1.png)

### Este trecho configura o ambiente necessário para um job ETL, incluindo a inicialização dos contextos do Spark e do Glue, e a preparação do job para execução.

![1](../evidencias/desafio/job2_tmdb/2.png)

### Este trecho de código define uma função que lê dados de um arquivo JSON, filtra registros com IDs de gênero Action/Adventure, verifica se há valores nulos e salva os dados filtrados no formato Parquet.

![1](../evidencias/desafio/job2_tmdb/3.png)

### Este trecho define uma variável execution_date que contém a data atual formatada.

![1](../evidencias/desafio/job2_tmdb/4.png)

### Este trecho configura os caminhos de entrada e saída para os dados JSON do TMDB, armazenando-os em um bucket S3 e organizando os dados processados em diretórios com base na data de execução.

![1](../evidencias/desafio/job2_tmdb/5.png)

### Este trecho  processa e salva os dados JSON do TMDB, exibindo uma mensagem de erro específica se ocorrer algum problema durante o processamento.

![1](../evidencias/desafio/job2_tmdb/6.png)

### Este trecho de código assegura que o job do AWS Glue seja devidamente encerrado, permitindo que o status do job seja atualizado e registrado no console do AWS Glue.

![1](../evidencias/desafio/job2_tmdb/7.png)

## 6. Execução do job "tmdb"

![1](../evidencias/desafio/job2_tmdb/8.png)

### Arquivos Parquet gerados pelo job "tmdb" do AWS Glue e salvos no bucket S3 na pasta correspondente à data de execução.

![1](../evidencias/desafio/job2_tmdb/9.png)



## 7. Athena - job "tmdb"

### Consulta dos dados "tmdb" armazenados no Amazon S3 usando SQL 

![1](../evidencias/desafio/athena_tmdb/1.png)

### Resultado da consulta

![1](../evidencias/desafio/athena_tmdb/2.png)



