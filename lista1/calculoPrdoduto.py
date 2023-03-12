"""
Um fabricante paga uma porcentagem de imposto sobre o total de uma venda
realizada. Esse fabricante conhece a quantidade de unidades de um produto que produziu
e o valor de cada peça. Ajude este fabricante escrevendo um programa em Python que
permita a leitura das seguintes informações: quantidade de unidades de um produto
produzidas, valor (preço) de uma unidade desse produto e porcentagem de imposto a ser
paga. Depois calcule o valor do imposto a ser pago e imprima na tela esse valor obtido.
"""

prod = int(input("Informe a quantidade de unidades: "))
preco = float(input("Informe o preço da unidade: "))
imposto = int(input("Porcentagem a ser paga: "))
calculoVendas = prod * preco
valorTotal = (calculoVendas * (imposto / 100))

print("O imposto é: ", valorTotal)