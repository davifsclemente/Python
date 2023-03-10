"""
Faça um programa em Python para converter um dado valor em reais (R$) para a
moeda dólar (US$). O programa deve ler um valor em reais (R$) e a cotação da moeda
americana, depois converter para dólares (US$) e apresentar este valor convertido na tela.
"""

valor = float(input("Informe a quantidade: "))
dolar = valor * 5.16

if 0 <= valor <= 1:
    print(valor, "equivale a", dolar, "Dólar americano")
else:
    print(valor, "equivale a", dolar, "Dólares americano")