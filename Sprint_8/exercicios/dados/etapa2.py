# Passo 1: Criar uma lista de 20 nomes de animais
animais = ["cachorro", "gato", "elefante", "tigre", "leão", "girafa", "cavalo", "coelho", "rato", "hamster",
           "papagaio", "canário", "peixe", "tartaruga", "cobra", "aranha", "macaco", "urso", "pato", "ovelha"]

# Passo 2: Ordenar a lista em ordem crescente
animais.sort()

# Passo 3: Imprimir cada item da lista
for animal in animais:
    print(animal)

# Passo 4: Armazenar o conteúdo da lista em um arquivo de texto no formato CSV
with open("animais.csv", "w") as arquivo:
    for animal in animais:
        arquivo.write(animal + "\n")
