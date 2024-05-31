 # Importa a biblioteca boto3 para interagir com os serviços da AWS
import boto3

def s3_select(bucket_name, file_key, query_expression, access_key_id, secret_access_key, session_token):
    try:
        # Configuração do cliente S3 com as credenciais fornecidas
        s3 = boto3.client(
            's3',
            aws_access_key_id=access_key_id,
            aws_secret_access_key=secret_access_key,
            aws_session_token=session_token,
            region_name='us-east-1'  
        )

         # Realiza a operação de SELECT no S3 usando uma expressão SQL
        response = s3.select_object_content(
            Bucket=bucket_name,
            Key=file_key,
            Expression=query_expression,
            ExpressionType='SQL',
            InputSerialization={'CSV': {'FileHeaderInfo': 'USE', 'RecordDelimiter': '\n'}},
            OutputSerialization={'CSV': {}},
        )

        # Lê e processa os resultados
        for event in response['Payload']:
            if 'Records' in event:
                # Decodifica os registros
                records = event['Records']['Payload']
                try:
                    records = records.decode('utf-8')
                except UnicodeDecodeError:
                    # Se houver um erro de decodificação, ignore este registro
                    continue
                # Divide os registros em linhas e exibe
                lines = records.split('\n')
                for line in lines:
                    if line:
                        print(line)
    
    except Exception as e:
        print("Ocorreu um erro ao executar a seleção:", e)

# Credenciais 
access_key_id = 'ASIAU6GDVVF6M6ET24WJ'
secret_access_key = '8FfbP2S1DCaHfbJQurK3+jC5BwKPrhM2Yrex3AUp'
session_token = 'IQoJb3JpZ2luX2VjEK3//////////wEaCXVzLWVhc3QtMSJGMEQCIGoOkyPVYhTX1AAIQZ1JvHACMjh7ytJ9C13b/4gEjMLuAiAC9Z9ACsgb9xEf8JVLBGdiitWZDS8iXfzqgs6QKHOkECqfAwg2EAAaDDMzOTcxMjc4MDY2OCIMDR6h48bvy0oA+tBIKvwCD1IHgltKnQ0pGI00Ru7hvB1ZTCNjX0zgNr/EdSo84WfFfx1k9YxfhcWdEj6tqx+6x7xvtPrnNpu7Is9PWb/Jo4CoqlNA7MNyL1Clz70/7lPPCpH1Pj30W6BY7WorlLu9KTl4PcrlOFkbWHMchrXyRaJ0h/g9oiz7CDDlo0Q8MJ7K9rVbDAy8c+dTWcJrcMDNH/Sv9rW2lGrjdqy8VUTPuAVCw10B0Tj8V4LJKoPFOilPb7Fsfp0Rox2VqsD94kVkTXl2GDLdchAJx8ry2Og6zonvFbhafQPCEIda+WdGItnBxJM6MXeE21VmpOyBISsTNgwRmVOcxgg+uSk3WI0T317g4+dklmKdveZHJlFKd4c0NYQ/WhQcQ4qTLftt6c/IqZ67J/A3hPXsA8/wLWHbGeX6p6RJaotK+gMn7cQS2c8GUTe0E+IbzRRjyX9CdijlCLPXlm//tDq8o9XSBCdQ/wZdAJQuR+ErVe8VFIsbs9ce4CxSvJFM+yX5i8MwhMHjsgY6pwG3Lfm21uDN/CD6KINojBxor22gJF/qnxYHMq+haEKYGrgiA37DadxDA+5x9xbRC0YL1LRSujJxQd5smQmqJ6OcRRMwd7FBn7sKkNmSJHZJOajIKw8kjnP8newiszmlCZen89g4vRxB1XqUvyEDcLc2lH7y6trncjDs6ZUy2SkKLVlY/m0MJjJesAQbWA1fPvGYdg46PUWiyN6RZdszj7PmHgEFCqzSTg=='

# Arquivo no S3
bucket_name = 'bucketangelicasprint5'
file_key = 'chegadas_2023_4.csv'

# Item 4.2 - Duas funções de Agregação - AVG e SUM
query_expression_1 = "SELECT AVG(CAST(chegadas AS FLOAT)) FROM s3object "
print("\nMédia Geral de Entrada de Estrangeiros no País:")
s3_select(bucket_name, file_key, query_expression_1, access_key_id, secret_access_key, session_token)
query_expression_2 = "SELECT SUM(CAST(chegadas AS FLOAT)) FROM s3object "
print("\nSoma de Entrada de Estrangeiros no País:")
s3_select(bucket_name, file_key, query_expression_2, access_key_id, secret_access_key, session_token)

# Item 4.1 - Claúsula filtra dois operadores lógicos - AND que verifica se o cod_continente esta entre 4 e 6  
# e o operador OR que verifica se é cod_continente = 1
# Item 4.3 -  CASE continente = EUROPA recebe EURO senão recebe DOLLAR | chegadas >= 169 recebe 'acima da media' 
# senão 'abaixo da média'
# Item 4.4 - CAST - INT inteiro e FLOAT para float
# Item 4.5 - DATE_ADD - adiciona quantidade de mês no ano
# Item 4.6 - Função string - UPPER - deixa letras maiusculas
query_expression_3 = '''SELECT 
                            UPPER(s.continente), 
                            s.pais, 
                            DATE_ADD(month, CAST(s.cod_mes AS INT), `2023T`),  
                            CASE s.continente WHEN 'Europa' 
                                THEN 'Euro' 
                                ELSE 'Dollar' 
                            END,
                            CASE WHEN CAST(chegadas AS FLOAT) >= 169 
                                THEN 'Acima da media' 
                                ELSE 'Abaixo da media' 
                            END 
                        FROM s3object AS s 
                        WHERE 
                            (CAST(s.cod_continente AS INT) >=4 
                            AND  
                            CAST(s.cod_continente AS INT) <=6)
                            OR 
                            CAST(s.cod_continente AS INT) = 1
                        LIMIT 10;'''
print("\nContinente | País | Data Registro | Moeda | Situação:")
#Executa uma consulta SQL em um arquivo armazenado em um bucket S3 e retorna os resultados dessa consulta
s3_select(bucket_name, file_key, query_expression_3, access_key_id, secret_access_key, session_token)
