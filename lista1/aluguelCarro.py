"""
Um grupo de amigos pretende alugar um carro por um único dia. Consultadas duas
agências, a primeira cobra R$62,00 pela diária e R$1,40 por quilômetro rodado. A segunda
cobra diária de R$80,00 e mais R$1,20 por quilômetro rodado. Escreva um programa em
Python que leia a quantidade de quilômetros a serem rodados e calcule e imprima na tela
o preço a ser pago em cada uma das agências.
"""

ag1 = 1.40
ag2 = 1.20
kmRodado = float(input("Informe quantos km você irá rodar: "))
total1 = kmRodado * 1.40
total2 = kmRodado * 1.20
if total1 > total2:
    print("O valor mais econômico é a Agência 1 ")
else:
    print("O valor mais econômico é a Agência 2 ")