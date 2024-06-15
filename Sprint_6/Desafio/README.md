
# Desafio
### Sobre o desafio:
O desafio é analisar um banco de dados para extrair informações específicas sobre séries e filmes do gênero ação/aventura. O objetivo é responder a questões definidas que nos permitam compreender melhor a história destes filmes e series, identificar modelos de popularidade, participação de artistas e outras características relevantes. 
Será feita uma análise para fornecer um panorama detalhado das séries e filmes de ação/aventura, facilitando a identificação das tendências recentes, da popularidade das séries e dos artistas, bem como da variedade de profissões envolvidas na produção, entre outros. Essas informações podem ser úteis para estudiosos de mídia, fãs de séries, filmes e profissionais da indústria do entretenimento que buscam entender melhor o mercado de séries de ação/aventura.

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


### Arquivos  
1. [Arquivo Python .py](../Desafio/teste.py)
2. [Arquivo Dockerfile](../Desafio/Dockerfile)
3. [Arquivo Docker-compose](../Desafio/docker-compose.yml)
4. [Arquivo Requeriments.txt](../Desafio/requirements.txt)
5. [Arquivo .env](../Desafio/.env)

# Evidências - Desafio
## Parte 1
### Código Python: 


#### Primeiro, importei as bibliotecas:

![1](../evidencias/desafio/python/1.png)

#### Usei o arquivo .env para salvar as credenciais da AWS: 

![2](../evidencias/desafio/python/2.png)

#### Verifica as credenciais:

![3](../evidencias/desafio/python/3.png)

#### Imprime as credencias para verificação do arquivo .env: 

![4](../evidencias/desafio/python/4.png)

#### Função 'def' para pode ler os arquivos CSV; definir o caminho e exibir os DataFrames:

![5](../evidencias/desafio/python/5.png)

#### Usando boto3, cria um cliente S3:

![6](../evidencias/desafio/python/6.png)

#### Define o nome do bucket, verifica se ele já existe, caso ele não exista, cria um novo:

![7](../evidencias/desafio/python/7.png)

#### Função que faz upload de arquivos CSV para o S3:

![8](../evidencias/desafio/python/8.png)


## Parte 2
### Execução do Código Python: 



#### Resumo: Lendo os arquivos CSV, acessando a AWS, criando Bucket e fazendo upload dos arquivos no bucket: 

![1](../evidencias/desafio/execucaopython/1.png)
![2](../evidencias/desafio/execucaopython/2.png)

#### Upload dos arquivos feito com sucesso para o bucket no S3:

![2](../evidencias/desafio/execucaopython/3.png)


## Parte 3
### Arquivo Dockerfile
#### Define a imagem Docker personalizada para construir um contêiner que executa um script Python:

![1](../evidencias/desafio/outros/dockerfile.png)

### Arquivo Docker-compose
#### Define a configuração para executar um serviço de contêiner Docker usando o Docker Compose:

![1](../evidencias/desafio/outros/dockercompose.png)

### Arquivo .env
#### Credenciais da AWS:

![1](../evidencias/desafio/outros/env.png)

### Arquivo Requirements
#### Lista as dependências do projeto código Python, definindo um conjunto de bibliotecas que são essenciais para o funcionamento do projeto python:

![1](../evidencias/desafio/outros/requirements.png)

### Organização na pasta

![1](../evidencias/desafio/outros/organizacao.png)

## Parte 4
### Execução do Docker

#### Comando 'docker-compose build', para constuir as imagens dos containers especificados no arquivo 'docker-compose.yml'. Lê o arquivo 'docker-compose.yml, constroi as imagens e armazena as imagens:

![1](../evidencias/desafio/dockerexecucao/1.png)
![2](../evidencias/desafio/dockerexecucao/2.png)

#### Comando 'docker compase up', responsavel por iniciar e executar os contêiners definidos no arquivo 'docker-compose.yml'. Ele lê os arquivos, contrói as imagens, cria e inicializa os contêiners, aguarda os  contêineres iniciarem e exibe os Log. Assim, Redes e contêineres necessários foram criados corretamente e o contêiner está em execução.

![3](../evidencias/desafio/dockerexecucao/3.png)

      
### Resultado no S3
#### Bucket e os arquivos:

![1](../evidencias/desafio/s3/1.png)
