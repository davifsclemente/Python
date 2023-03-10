"""
Escreva um programa em Python que calcule o valor do desconto de uma mercadoria
paga a vista e o valor total a ser pago. O programa deve ler o valor da mercadoria e a
porcentagem do desconto. Depois o programa deve calcular e imprimir na tela o valor do
desconto e o novo valor da mercadoria com o desconto.
"""

valorTotal = float(input("Informe o valor total: "))
valorDesconto = float(input("Informe o valor do desconto: "))
valorDescontado = valorTotal * (valorDesconto / 100)
print("O desconto é de:", valorDescontado)
novoValorTotal = valorTotal - valorDescontado
print("ovo valor do produto é: ", novoValorTotal)