"""
Escreva um programa em Python que leia o peso e a altura de uma pessoa. Em
seguida o programa deve calcular e imprimir índice de massa corpórea (IMC) dessa
pessoa. Dado:
IMC =peso / altura+*2
"""

p = float(input("Informe o seu peso: "))
h = float(input("informe sua altura: "))
imc = p / (h**2)
print("Seu IMC é: ", imc)