"""
11. Escreva um programa em Python que leia os valores da base maior (B), base menor
(b) e altura (h) de um trapézio e calcule e imprima o valor de sua área, sabendo que a área
de um trapézio (A) é dada por:
A = (B + b) * h
        2
"""

B = float(input("informe o lado maior: "))
b = float(input("informe o lado menor: "))
h = float(input("informe a altura: "))
A = ((B + b) * h) / 2

print("Area: ", A)