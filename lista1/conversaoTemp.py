"""
Faça um programa em Python que leia uma temperatura fornecida em graus fahrenheit
e a converta para o seu equivalente em graus centígrados, imprimindo este valor na tela.
Dado:
C = 5 / 9 * (F − 32)
"""

temp = float(input("Informe a temperatura: "))
c = 5 / 9 * (temp - 32)
print("A temperatura em Celsius, e: ", c)