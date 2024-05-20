

# Exercício 1

with open('number.txt') as data:
    numeros = list(map(int, data.readlines()))

pares = list(filter(lambda x: x % 2 == 0, numeros))
pares_ordenados = sorted(pares, reverse=True)
cinco_maiores = pares_ordenados[:5]
soma_cinco_maiores = sum(cinco_maiores)

print(cinco_maiores)
print(soma_cinco_maiores)




# Exercício 2

def conta_vogais(texto: str) -> int:
    eh_vogal = lambda x: x.lower() in 'aeiou'
    numero_vogais = len(list(filter(eh_vogal, texto)))
    return numero_vogais

texto_teste = "Python is awesome"
print("Número de vogais:", conta_vogais(texto_teste))




# Exercício 3

from functools import reduce

def calcula_saldo(lancamentos) -> float:
    valores_mapeados = map(lambda x: x[0] if x[1] == 'C' else -x[0], lancamentos)
    saldo_final = reduce(lambda x, y: x + y, valores_mapeados, 0)
    return saldo_final

lancamentos = [
    (200, 'D'),
    (300, 'C'),
    (100, 'C')
]

print("Saldo final:", calcula_saldo(lancamentos))




# Exercício 4

def calcular_valor_maximo(operadores, operandos) -> float:
    resultados = list(map(lambda x: eval(f'{x[0][0]}{x[1]}{x[0][1]}'), zip(operandos, operadores)))
    return max(resultados)

operadores = ['+', '-', '*', '/', '+']
operandos = [(3, 6), (-7, 4.9), (8, -8), (10, 2), (8, 4)]

print("Maior valor resultante:", calcular_valor_maximo(operadores, operandos))




# Exercício 5

def processar_dados_estudantes(caminho_arquivo):
    with open(caminho_arquivo, 'r') as arquivo_csv:
        linhas = arquivo_csv.readlines()

    linhas = sorted(linhas)

    for linha in linhas:
        dados = linha.strip().split(',')
        nome_estudante = dados[0]
        notas = list(map(int, dados[1:]))
        notas = sorted(notas, reverse=True)
        tres_maiores_notas = notas[:3]
        media = round(sum(tres_maiores_notas) / len(tres_maiores_notas), 2)

        print(f"Nome: {nome_estudante} Notas: {tres_maiores_notas} Média: {media}")

processar_dados_estudantes("estudantes.csv")




# Exercício 6

def maiores_que_media(conteudo: dict) -> list:
    media = sum(conteudo.values()) / len(conteudo)
    produtos_acima_media = [(produto, preco) for produto, preco in conteudo.items() if preco > media]
    produtos_acima_media.sort(key=lambda x: x[1])
    return produtos_acima_media




# Exercício 7

def pares_ate(n: int):
    n = max(2, n)
    for i in range(2, n + 1, 2):
        yield i