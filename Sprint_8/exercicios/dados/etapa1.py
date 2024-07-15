import random

# Passo 1: Criar uma lista de 250 inteiros aleatórios
lista = [random.randint(0, 1000) for _ in range(250)]

# Passo 2: Reverter a lista
lista.reverse()

# Passo 3: Imprimir o resultado
print(lista)
