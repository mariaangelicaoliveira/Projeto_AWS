## Desafio 

### Etapa 1

 -  Iniciando um novo container e copiando o script python:
 
        Docker run - inicia

        -d - executa em segundo plano

        --name - define o nome

        cp - copia 

![1](../evidencias/1_etapa/1_criandocontainer.png)


- Criando um arquivo Dockerfile para executar o script python carguru.py:

![2](../evidencias/1_etapa/2_dockerfile.png)


- Build - Criando uma imagem a partir de um arquivo Dockerfile:

![3](../evidencias/1_etapa/3_build.png)


- Rodando a imagem:

![4](../evidencias/1_etapa/4_rodandoimagem.png)


- Localhost:

![5](../evidencias/1_etapa/5_localhost.png)



### Etapa 2


-  Reiniciando:
  
       Docker stop - para de rodar
       Docker start - reinicia 

![6](../evidencias/2_etapa/5_reiniciando.png)



### Etapa 3


- Criando um arquivo Dockerfile:


![7](../evidencias/3_etapa/1_dockerfile.png)


- Criando um script python:


![8](../evidencias/3_etapa/2_script.png)


- Iniciando um novo container e copiando o script python:
 
       Docker run - inicia

       -d - executa em segundo plano

       --name - define o nome

       cp - copia 


![9](../evidencias/3_etapa/3_container.png)


- Build - Criando uma imagem a partir de um arquivo Dockerfile:


![10](../evidencias/3_etapa/4_build.png)


- Renomeando imagem:


![11](../evidencias/3_etapa/5_renomeando.png)


![12](../evidencias/3_etapa/6_renomeando.png)


- Inicia o container:
       
       docker run
      -it - de maneira interativa


![13](../evidencias/3_etapa/7_rodando.png)


- Arquivos etapa 1 e 2: 
1. [carguru.py](../Desafio/parte_1/carguru.py)
2. [Dockerfile](../Desafio/parte_1/Dockerfile)

- Arquivos etapa 3:

1. [script.py](../Desafio/parte_2/script.py)
2. [Dockerfile](../Desafio/parte_2/Dockerfile)