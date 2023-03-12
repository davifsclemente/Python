"""
Faça um programa em Python que leia a idade de uma pessoa expressa em anos,
meses e dias e mostre-a expressa apenas em dias. Assuma, neste programa, que um ano
tem 365 dias e que um mês tem 30 dias. Exemplo: Se a pessoa digitar que tem 28 anos 1
mês e 10 dias deverá aparecer na tela que ela viveu 10260 dias
"""

diasVividos = int(input("Informe quantos dias você acha que viveu: "))
ano = diasVividos // 365
rst = diasVividos % 365
mes = rst // 30
dia = rst % 30

print("Você viveu", ano, "anos,", mes, "meses", dia, "dias.")