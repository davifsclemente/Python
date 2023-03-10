"""
Sabe-se que para iluminar de maneira correta os cômodos de uma casa, para cada m2
deve-se usar 18 W de potência. Escreva um programa em Python que leia as dimensões
de um cômodo retangular (em metros), calcule e mostre a sua área (em m2) e a potência
de iluminação que deverá ser utilizada.
"""

p = 18
b = float(input("Informe o tamanho da base: "))
h = float(input("Informe a altura: "))
d = 18 * (b * h)
print("Será necessário", d, "W de potência.")
