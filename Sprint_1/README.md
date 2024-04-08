# Exercícios

## Problema a ser resolvido:
- Criar um arquivo executável “.sh” com uma lista de comandos
- Agendar a execução do arquivo “.sh” no “crontab”.
- Gerar relatórios de vendas e um relatório final. 

## Como você resolveu?
    Primeiro, usei o comando cat para criar  e abrir o arquivo executável .sh:
    Dentro do arquivo .sh escrevi os comandos necessários para sua execução
    Agendei a execução do arquivo .sh dentro do arquivo crontab e também executei o comando sudo chmod +x para dar permissão ao sistema acessar o .sh.
    Para modificar o conteúdo da lista do arquivo .csv usei o chat gpt, para que ele criasse listas aleatórias. Para verificar se o arquivo .sh estava agendado corretamente, mudei a data e o horário do sistema para rodar automaticamente no horário solicitado no desafio. Posteriormente, criei um arquivo novo .sh com comandos para gerar um relatório final e os executei manualmente no terminal.

## Detalhes do código:

#### Usando o programa VS Code

#### Criei o arquivo “processamento_de_vendas.sh” usando o comando:
`Cat > /home/ang/MariaAngelica_DA/Sprint_1/exercícios/processamento_de_vendas.sh`

### Dentro do arquivo processamento_de_vendas.sh, editei o código:

##### Criando diretório vendas:
`mkdir -p /home/ang/MariaAngelica_DA/Sprint_1/exercicios/vendas`

##### Copiando o arquivo (dados vendas) do diretório ecommerce para o diretório vendas 
`cp/home/ang/MariaAngelica_DA/Sprint_1/exercicios/ecommerce/dados_de_vendas.csv /home/ang/MariaAngelica_DA/Sprint_1/exercicios/vendas`

##### ENTRAR NO DIRETORIO VENDAS     
`cd /home/ang/MariaAngelica_DA/Sprint_1/exercicios/vendas`

##### CRIAR DIRETORIO BACKUP DENTRO DO DIRETORIO VENDAS
`mkdir -p /home/ang/MariaAngelica_DA/Sprint_1/exercicios/vendas/backup`

##### COPIAR ARQUIVO CSV PARA O DIRETORIO BACKUP
`cp dados_de_vendas.csv backup/`

##### ENTRAR NO DIRETORIO BACKUP
`cd /home/ang/MariaAngelica_DA/Sprint_1/exercicios/vendas/backup`

##### RENOMEAR ARQUIVO CSV 
`mv dados_de_vendas.csv dados-"$(date +'%Y%m%d')".csv`

##### RENOMEAR ARQUIVO CSV
`mv dados-"$(date +'%Y%m%d')".csv backup-dados-"$(date +'%Y%m%d')".csv`

##### CRIAR ARQUIVO TXT 
`touch relatorio.txt`

##### DATA DO SISTMA OPERACIONAL
`echo "\n Data de Execucao" >> relatorio.txt – especifica a informação `

`date +"%Y/%m/%d %H:%M" >> relatorio.txt`

##### DATA DA PRIMEIRA VENDA
`echo "\n Data primeira venda" >> relatorio.txt `

`cut -d ',' -f 5 backup-dados-"$(date +'%Y%m%d')".csv | head -2 | tail -1 >> relatorio.txt`

##### DATA DA ULTIMA VENDA
`echo "\n Data Ultima venda" >> relatorio.txt`

`cut -d ',' -f 5 backup-dados-"$(date +'%Y%m%d')".csv | tail -1 >> relatorio.txt`

##### QUANTIDADE DE PRODUTOS UNICOS 
`echo "\n Quantidade de Produtos Unicos" >> relatorio.txt`

`cut -d ',' -f 2 backup-dados-"$(date +'%Y%m%d')".csv |sort | uniq -i | wc -l >> relatorio.txt`

##### PRIMEIROS REGISTROS – head = réd
`echo "\n 10 primeiros registros" >> relatorio.txt`

`head -n11 backup-dados-"$(date +'%Y%m%d')".csv >> relatorio.txt`

##### COMPRIMIR ARQUIVO CSV
`zip backup-dados-"$(date +'%Y%m%d')".zip backup-dados-"$(date +'%Y%m%d')".csv`

##### DELETAR ARQUIVOS
`rm backup-dados-"$(date +'%Y%m%d')".csv `

`rm ../dados_de_vendas.csv`

### No terminal:

#### Agendamento execução:

`Sudo chmod +x processamento_de_vendas.sh`

`Crontab -e – min/hora/dia/mês/dia da semana`

`27 15 * * 1-4 home/ang/MariaAngelica_DA/Sprint_1/exercícios/processamento_de_vendas.sh`

### Criacao script novo:
`Cat > consolidador_de_processo_de_vendas.sh`

### Dentro do arquivo consolidador_de_vendas.sh: 
~~~
touch /home/ang/MariaAngelica_DA/Sprint_1/exercicios/relatorio_final.txt

cat /home/ang/MariaAngelica_DA/Sprint_1/exercicios/vendas/backup/relatorio.txt >> /home/ang/MariaAngelica_DA/Sprint_1/exercicios/relatorio_final.txt
~~~
# Pq que resolveu desta forma?
Utilizando o conhecimento adquirido nos cursos de Linux e Git e GitHub e com auxílio de fóruns de comando Linux e chat gpt, com tentativas com vários erros e acertos, conclui que essa era maneira mais funcional para resolução do desafio.

# Dificuldades?
Sim, como o aprendizado nos cursos da udemy eram de forma mais abrangente, tive que procurar em fóruns, consultei membros da squad e outras fontes para resolver alguns problemas e desafios, de forma geral os cursos deram uma boa base para que pudesse entender como e onde procurar e como proceder para resolução do desafio, acredito que meu conhecimento atual foi resultado da junção do curso e prática de resolução de problemas reais.

Código em execução:

### Criar arquivo .sh:
Cat > /home/ang/MariaAngelica_DA/Sprint_1/exercícios/processamento_de_vendas.sh

## Conteudo do arquivo Processamento_de_vendas.sh:
~~~
mkdir -p /home/ang/MariaAngelica_DA/Sprint_1/exercicios/vendas
cp /home/ang/MariaAngelica_DA/Sprint_1/exercicios/ecommerce/dados_de_vendas.csv /home/ang/MariaAngelica_DA/Sprint_1/exercicios/vendas
cd /home/ang/MariaAngelica_DA/Sprint_1/exercicios/vendas
mkdir -p /home/ang/MariaAngelica_DA/Sprint_1/exercicios/vendas/backup
cp dados_de_vendas.csv backup/
cd /home/ang/MariaAngelica_DA/Sprint_1/exercicios/vendas/backup
mv dados_de_vendas.csv dados-"$(date +'%Y%m%d')".csv
mv dados-"$(date +'%Y%m%d')".csv backup-dados-"$(date +'%Y%m%d')".csv
touch relatorio.txt
echo "\n Data de Execucao" >> relatorio.txt
date +"%Y/%m/%d %H:%M" >> relatorio.txt
echo "\n Data primeira venda" >> relatorio.txt
cut -d ',' -f 5 backup-dados-"$(date +'%Y%m%d')".csv | head -2 | tail -1 >> relatorio.txt
echo "\n Data Ultima venda" >> relatorio.txt
cut -d ',' -f 5 backup-dados-"$(date +'%Y%m%d')".csv | tail -1 >> relatorio.txt
echo "\n Quantidade de Produtos Unicos" >> relatorio.txt
cut -d ',' -f 2 backup-dados-"$(date +'%Y%m%d')".csv |sort | uniq -i | wc -l >> relatorio.txt
echo "\n 10 primeiros registros" >> relatorio.txt
head -n11 backup-dados-"$(date +'%Y%m%d')".csv >> relatorio.txt
zip backup-dados-"$(date +'%Y%m%d')".zip backup-dados-"$(date +'%Y%m%d')".csv
rm backup-dados-"$(date +'%Y%m%d')".csv 
rm ../dados_de_vendas.csv
~~~

### Agendamento execução:
`Sudo chmod +x processamento_de_vendas.sh`

`Crontab -e`

`27 15 * * 1-4 home/ang/MariaAngelica_DA/Sprint_1/exercícios/processamento_de_vendas.sh`

### Criacao script novo:
Cat > consolidador_de_processo_de_vendas.sh

### Dentro do arquivo consolidador_de_vendas.sh:
~~~
touch /home/ang/MariaAngelica_DA/Sprint_1/exercicios/relatorio_final.txt
cat /home/ang/MariaAngelica_DA/Sprint_1/exercicios/vendas/backup/relatorio.txt >> /home/ang/MariaAngelica_DA/Sprint_1/exercicios/relatorio_final.txt
~~~



# Evidências

[Código do Arquivo Processamento_de_vendas.sh:](evidencias/codigo_arquivo_processamento_de_vendas.png)

[Criando agendamento de execução:](evidencias/Criando_agendamento_de_execucao.png)

[Teste executar em 5 em 5 min - log](evidencias/teste_log.png)

[Agendamento 15:27 se segunda a quinta:](evidencias/agendamento_15_27-1-4.png)

[Relatório gerado do agendamento: 1](evidencias/relatorio_agendamento1.png)

[Relatório gerado do agendamento: 2](evidencias/relatorio_agendamento2.png)

[Relatório gerado do agendamento: 3](evidencias/relatorio_agendamento3.png)

[Script consolidador_de_processo_de_vendas.sh:](evidencias/Script_consolidador_de_processo_de_vendas.png)

[Pastas e arquivos criados na execução dos comandos do desafio da sprint 1:](evidencias//resultado_pastas_arquivos.png)

[Relatório final: 1](evidencias/relatorio_final.png)

[Relatório final: 2](evidencias/relatorio_final2.png)

<!-- ![Evidencia 1](evidencias/'nome'.webp) -->