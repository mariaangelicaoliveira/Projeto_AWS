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






