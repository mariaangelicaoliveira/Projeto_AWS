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
access_key_id = 'ASIAU6GDVVF6P2RXPMTL'
secret_access_key = 'CGjWMdFN5Q9ycyX/XLQtieeQECy5Nsp65qreCLga'
session_token = 'IQoJb3JpZ2luX2VjEML//////////wEaCXVzLWVhc3QtMSJIMEYCIQCEkkFoK7+vtLza+TY7DkZ8THlLmorf8XU0jFAwIbXGsgIhAIULJDZmNssF4eRf3sp0f+ohSvTGbokG5hnSr1EO8bS+Kp8DCEoQABoMMzM5NzEyNzgwNjY4Igwm/T3AQwBWw2ZVcSYq/AJbec+Ki6bjCNYKSc8POJdClZ2mqFU4aVrLJlD3aHiIMD/51xHwDKAZIlA9B7+KP8z3O7eSMvnuakV2KE3On6KCPajwnwGJtICtKQvftTealeWIMJ3KU09G33EcqTwX2IrlniIckdiwqocPfY29kWTjxyd/4Z5TwjUVpBIbgpZuUIdnaStYZbJfZMhRqd7dp3vhwE9qKFWFnPANNLqeyNjr1AmLDPp1leqelWPtcSpqH5nAbKgOyCmw6d8Nk4MUIVSRKPXP7EOebDAuj84u7QHinpTn5nlPMpcf0cuBtZzrh5peC9OLm0EjDZ34DFnYNoIRG2V9NtI1ra6Yx66Xy+Tz3EZn/QfopW4cZtjT235qsN0zZx/Oyh2GGUfhnsAmWRsXWH5yvqkOQqe4L8VzN7YVT1O7vOU89ZleAI2xgoDn0rR3NAciGJ4P4OwwFcIagsyg86JZ+hDwhZzb1r0g6YM3TlR0D95zVJWzUvC21WDtLa9imgfGDtrblNnsGzDSjeiyBjqlAbswRBSAs/t6hL+lVhZ58Pu5CJWWrH/ghl9Cc+kc3hb+Zd8V16UTl8sAhtpqWCdMuzs/+1xUcZRON3Iy7+M7udyEDdm4LW8eJWgmbyk4Jh711HLwWHwCWYrNCIWIw05dN/CePXVWeNEGB/SKJ6p4RkU0fQeZByVz7krd7xp3Cevhw7zVJ6dxFoecGjL/qbQtChq5ZWdjGsIju4hUjttcX4S9C3ptKw=='

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
# Item 4.3 - função condicional - CASE continente = EUROPA recebe EURO senão recebe DOLLAR | chegadas >= 169 recebe 'acima da media' 
# senão 'abaixo da média'
# Item 4.4 - função de conversão - CAST - INT inteiro e FLOAT para float
# Item 4.5 - função data - DATE_ADD - adiciona quantidade de mês no ano
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
