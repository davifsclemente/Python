"""
O custo ao consumidor de um carro novo é a soma do custo de fábrica com a
porcentagem do distribuidor e dos impostos (aplicados ao custo de fábrica). Supondo que
a porcentagem do distribuidor seja de 28% e os impostos de 45%, escreva um programa
em Python que leia o custo de fábrica de um carro e escreva o custo ao consumidor.
"""

custoDist = (28/100)
imposto = (45/100)
custoFab = float(input("Quanto a fábrica gastou: "))
total = custoFab + custoDist + imposto
print("O custo mínimo pro cliente é de: ", total)