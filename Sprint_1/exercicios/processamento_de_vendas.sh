#CRIAR DIRETORIO VENDAS
mkdir -p /home/ang/MariaAngelica_DA/Sprint_1/exercicios/vendas
#COPIAR ARQUIVO CSV DO DIRETORIO ECOMMERCE PARA O DIRETORIO VENDAS
cp /home/ang/MariaAngelica_DA/Sprint_1/exercicios/ecommerce/dados_de_vendas.csv /home/ang/MariaAngelica_DA/Sprint_1/exercicios/vendas
#ENTRAR NO DIRETORIO VENDAS 
cd /home/ang/MariaAngelica_DA/Sprint_1/exercicios/vendas
#CRIAR DIRETORIO BACKUP DENTRO DO DIRETORIO VENDAS
mkdir -p /home/ang/MariaAngelica_DA/Sprint_1/exercicios/vendas/backup
#COPIAR ARQUIVO CSV PARA O DIRETORIO BACKUP
cp dados_de_vendas.csv backup/
#ENTRR NO DIRETORIO BACKUP
cd /home/ang/MariaAngelica_DA/Sprint_1/exercicios/vendas/backup
#RENOMEAR ARQUIVO CSV
mv dados_de_vendas.csv dados-"$(date +'%Y%m%d')".csv
#RENOMEAR ARQUIVO CSV
mv dados-"$(date +'%Y%m%d')".csv backup-dados-"$(date +'%Y%m%d')".csv
#CRIAR ARQUIVO TXT
touch relatorio.txt
#DATA DO SISTMA OPERACIONAL
echo "\n Data de Execucao" >> relatorio.txt
date +"%Y/%m/%d %H:%M" >> relatorio.txt
#DATA DA PRIMEIRA VENDA
echo "\n Data primeira venda" >> relatorio.txt
cut -d ',' -f 5 backup-dados-"$(date +'%Y%m%d')".csv | head -2 | tail -1 >> relatorio.txt
#DATA DA ULTIMA VENDA
echo "\n Data Ultima venda" >> relatorio.txt
cut -d ',' -f 5 backup-dados-"$(date +'%Y%m%d')".csv | tail -1 >> relatorio.txt
#QUANTIDADE DE PRODUTOS UNICOS
echo "\n Quantidade de Produtos Unicos" >> relatorio.txt
cut -d ',' -f 2 backup-dados-"$(date +'%Y%m%d')".csv |sort | uniq -i | wc -l >> relatorio.txt
#10 PRIMEIROS REGISTROS
echo "\n 10 primeiros registros" >> relatorio.txt
head -n11 backup-dados-"$(date +'%Y%m%d')".csv >> relatorio.txt
#COMPRIMIR ARQUIVO CSV
zip backup-dados-"$(date +'%Y%m%d')".zip backup-dados-"$(date +'%Y%m%d')".csv
#DELETAR ARQUIVO
rm backup-dados-"$(date +'%Y%m%d')".csv 
rm ../dados_de_vendas.csv






