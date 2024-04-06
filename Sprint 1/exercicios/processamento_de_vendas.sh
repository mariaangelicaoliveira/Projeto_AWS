#1
mkdir -p vendas
cp ecommerce/* vendas
#2
cd vendas
mkdir -p backup
cp dados_de_vendas.csv backup/
cd backup
mv dados_de_vendas.csv dados-"$(date +'%Y%m%d')".csv
#3
mv dados-"$(date +'%Y%m%d')".csv backup-dados-"$(date +'%Y%m%d')".csv
#4
touch relatorio.txt
#4.1
date +"%Y/%m/%d %H:%M" >> relatorio.txt
#4.2
echo "\n Data primeira venda" >> relatorio.txt
cut -d ',' -f 5 backup-dados-"$(date +'%Y%m%d')".csv | head -2 | tail -1 >> relatorio.txt
#4.3
echo "\n Data Ultima venda" >> relatorio.txt
cut -d ',' -f 5 backup-dados-"$(date +'%Y%m%d')".csv | tail -1 >> relatorio.txt

echo "\n Quantidade de Produtos Unicos" >> relatorio.txt
cut -d ',' -f 2 backup-dados-"$(date +'%Y%m%d')".csv |sort | uniq -i | wc -l >> relatorio.txt
#echo "2024/04/04 - 13:31" > relatorio.txt
cat backup-dados-"$(date +'%Y%m%d')".csv | head -2 | tail -1 >> relatorio.txt
cat backup-dados-"$(date +'%Y%m%d')".csv | tail -2 | head -1 >> relatorio.txt
#head -n '2p' backup-dados-20240403.csv >> relatorio.txt
#tail -n 2 backup-dados-20240403.csv >> relatorio.txt
#echo "2023/01/01\n2023/03/27\n68" >> relatorio.txt
sort backup-dados-"$(date +'%Y%m%d')".csv | uniq -1 >> relatorio.txt
head -n10 backup-dados-"$(date +'%Y%m%d')".csv >> relatorio.txt
zip backup-dados-"$(date +'%Y%m%d')".zip backup-dados-"$(date +'%Y%m%d')".csv
rm backup-dados-"$(date +'%Y%m%d')".csv 
rm ../dados_de_vendas.csv







