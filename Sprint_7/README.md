

# Evidências - Exercícios



## SPARK

### Parte 1 

![1](evidencias/Exercicio/spark/1.png)

### Parte 2

![1](evidencias/Exercicio/spark/2.png)

### Parte 3

![1](evidencias/Exercicio/spark/3.png)

### Parte 4

![1](evidencias/Exercicio/spark/4.png)

### Parte 5

![1](evidencias/Exercicio/spark/5.png)


### Parte 6

![1](evidencias/Exercicio/spark/9.png)

### Parte 7

![1](evidencias/Exercicio/spark/10.png)

### Parte 8

![1](evidencias/Exercicio/spark/11.png)


## LAB GLUE

### Parte 1 

![1](evidencias/Exercicio/labglue/config/1.png)

### Parte 2

![1](evidencias/Exercicio/labglue/config/2.png)

### Parte 3

![1](evidencias/Exercicio/labglue/config/3.png)

### Parte 4

![1](evidencias/Exercicio/labglue/config/4.png)

### Parte 5

![1](evidencias/Exercicio/labglue/config/5.png)

### Parte 6

![1](evidencias/Exercicio/labglue/config/6.png)

### Parte 7

![1](evidencias/Exercicio/labglue/config/7.png)

### Parte 8

![1](evidencias/Exercicio/labglue/config/8.png)

### Parte 9

![1](evidencias/Exercicio/labglue/config/9.png)

### Parte 10

![1](evidencias/Exercicio/labglue/cod/1.png)

### Parte 11

![1](evidencias/Exercicio/labglue/cod/2.png)

### Parte 12

![1](evidencias/Exercicio/labglue/cod/3.png)

### Parte 13

![1](evidencias/Exercicio/labglue/cod/4.png)





# Evidências - Desafio

### Arquivos  
1. [Arquivo Python Desafio](Desafio/etapas/complement_data.py)


## Parte 1
### API TMDB: 


#### Criei uma conta no site TMDB e criei uma API:

![1](evidencias/Desafio/tmdb/1.png)




## Parte 2
### Arquivo .env e Código Python: 


#### Usei o arquivo .env  para armazenar informações sensíveis, como chaves de API e credenciais, de forma segura. 

![1](evidencias/Desafio/codigopy/0.png)

#### Imports de bibliotecas para configur o ambiente para realizar tarefas como a interação com serviços da AWS entre outras funcionalidades necessárias para o funcionamento do script.

![1](evidencias/Desafio/codigopy/1.png)

#### Carrega Informações das chave da API e credenciais da AWS

![1](evidencias/Desafio/codigopy/2.png)

#### Carrega variáveis de ambiente usando a biblioteca os, útil para garantir que as informações sensíveis não estejam  no código, tornando mais seguro. 

![1](evidencias/Desafio/codigopy/3.png)

#### Essa abordagem assegura que as credenciais sensíveis sejam usadas de forma segura e que as operações S3 sejam configuradas corretamente para o ambiente específico.

![1](evidencias/Desafio/codigopy/4.png)

#### A função Lambda lambda_handler interage com a API do TMDB para obter dados sobre filmes populares e armazena esses dados no Amazon S3 em lotes de 100 registros. Ela começa configurando a URL da API do TMDB e os parâmetros necessários, faz uma requisição GET e processa a resposta JSON. Os dados são organizados por data e divididos em lotes, que são então carregados no S3. O código inclui tratamento de exceções para lidar com erros de credenciais da AWS, problemas na requisição à API do TMDB e outros erros genéricos, garantindo a robustez e a segurança da operação.

![1](evidencias/Desafio/codigopy/5.png)

#### Permite que você teste a função Lambda localmente, verificando seu comportamento e a saída sem precisar implantá-la na AWS.

![1](evidencias/Desafio/codigopy/6.png)

#### Executando o código 

![1](evidencias/Desafio/codigopy/7.png)


![1](evidencias/Desafio/codigopy/8.png)


### Lab AWS
### Lambda

#### Função Lambda
![1](evidencias/Desafio/lambda/1.png)

#### Executando o código na AWS Lambda
![1](evidencias/Desafio/lambda/2.png)
![1](evidencias/Desafio/lambda/3.png)

### Amazon Event Bridge

#### Agendando extrações periódicas de dados de forma automática usando Amazon Event Bridge

![1](evidencias/Desafio/AmazonEventBridge/1.png)

### S3

#### Resultao no S3
![1](evidencias/Desafio/s3/s3print.png)




# Perguntas


### Perguntas dos filmes de ação/aventura:

1. Quais são os títulos principais de filmes do gênero ação/aventura lançados nos últimos 10 anos?
2. Quais são os artistas que participaram de mais de um filme do gênero ação/aventura?
3. Quais são os filmes de ação/aventura com a maior nota média e mais de 1000 votos?
4. Quais são as profissões dos artistas que trabalharam em filmes de ação/aventura?  
5. Quais são os personagens principais dos filmes de ação/aventura que têm mais de 120 minutos de duração?

### Perguntas das séries de ação/aventura:

1. Quais são as séries do gênero ação/aventura lançadas nos últimos 5 anos?
2. Quais são os artistas que participaram de mais de uma série do gênero ação/aventura?
3. Quais são as séries de ação/aventura com a maior nota média e mais de 500 votos?
4. Quais são as profissões dos artistas que trabalharam em séries de ação/aventura?
5. Quais são os personagens principais das séries de ação/aventura que têm mais de 45 minutos de duração por episódio?


# Certificados


Essa Sprint não teve cursos da AWS para obter certificados.



