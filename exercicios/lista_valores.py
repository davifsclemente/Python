import math

nome = input("Nome: ")
mat = int(input("Matrícula: "))

listaDeNumeros1 = [3, 2, 4, 12, 4, 1, 4, 12]
listaDeNumeros2 = [8, 10, 11, 4, 2, 5, 4, 7]
listaDeNumeros3 = [3, 6, 1, 5, 6, 6, 5, 5]
listaDeNumeros4 = [12, 8, 3, 7, 11, 8, 9, 9]
listaDeNumeros5 = [5, 12, 7, 5, 5, 9, 4, 11]
listaDeNumeros6 = [11, 8, 11, 7, 4, 11, 12, 4]

soma = sum(listaDeNumeros1)
div = (soma / len(listaDeNumeros1))

print("\nRegistro 1: ", div)

for i in range(len(listaDeNumeros1)):
    listaDeNumeros1[i] = (i - div)**2
soma = sum(listaDeNumeros1)
div = (soma / len(listaDeNumeros1))

print("Registro 2: ", div)

raiz = math.sqrt(div)

print("Registro 3: ", raiz)

soma = sum(listaDeNumeros2)
div = (soma / len(listaDeNumeros2))

print("\nRegistro 1: ", div)

for i in range(len(listaDeNumeros2)):
    listaDeNumeros2[i] = (i - div)**2
soma = sum(listaDeNumeros2)
div = (soma / len(listaDeNumeros2))

print("Registro 2: ", div)

raiz = math.sqrt(div)

print("Registro 3: ", raiz)

soma = sum(listaDeNumeros3)
div = (soma / len(listaDeNumeros3))

print("\nRegistro 1: ", div)

for i in range(len(listaDeNumeros3)):
    listaDeNumeros3[i] = (i - div)**2
soma = sum(listaDeNumeros3)
div = (soma / len(listaDeNumeros3))

print("Registro 2: ", div)

raiz = math.sqrt(div)

print("Registro 3: ", raiz)

soma = sum(listaDeNumeros4)
div = (soma / len(listaDeNumeros4))

print("\nRegistro 1: ", div)

for i in range(len(listaDeNumeros4)):
    listaDeNumeros4[i] = (i - div)**2
soma = sum(listaDeNumeros4)
div = (soma / len(listaDeNumeros4))

print("Registro 2: ", div)

raiz = math.sqrt(div)

print("Registro 3: ", raiz)

soma = sum(listaDeNumeros4)
div = (soma / len(listaDeNumeros4))

print("\nRegistro 1: ", div)

for i in range(len(listaDeNumeros4)):
    listaDeNumeros4[i] = (i - div)**2
soma = sum(listaDeNumeros4)
div = (soma / len(listaDeNumeros4))

print("Registro 2: ", div)

raiz = math.sqrt(div)

print("Registro 3: ", raiz)

soma = sum(listaDeNumeros5)
div = (soma / len(listaDeNumeros5))

print("\nRegistro 1: ", div)

for i in range(len(listaDeNumeros5)):
    listaDeNumeros5[i] = (i - div)**2
soma = sum(listaDeNumeros5)
div = (soma / len(listaDeNumeros5))

print("Registro 2: ", div)

raiz = math.sqrt(div)

print("Registro 3: ", raiz)

soma = sum(listaDeNumeros6)
div = (soma / len(listaDeNumeros6))

print("\nRegistro 1: ", div)

for i in range(len(listaDeNumeros6)):
    listaDeNumeros6[i] = (i - div)**2
soma = sum(listaDeNumeros6)
div = (soma / len(listaDeNumeros6))

print("Registro 2: ", div)

raiz = math.sqrt(div)

print("Registro 3: ", raiz)