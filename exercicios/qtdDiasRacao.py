peso = float(input("Informe o peso do cachorro: "))
pesoRacao = float(input("Informe o peso do pacote de ração: "))

if peso < 5:
    tempo = pesoRacao // 60000
    print("O tempo que o saco de ração vai durar, é: ", tempo)
elif 6 <= peso <= 10:
    tempo = pesoRacao // 95000
    print("O tempo que o saco de ração vai durar, é: ", tempo)
elif 11 <= peso <= 15:
    tempo = 135000
    print("O tempo que o saco de ração vai durar, é: ", tempo)
elif 16 <= peso <= 20:
    tempo = pesoRacao // 170000
    print("O tempo que o saco de ração vai durar, é: ", tempo)
else:
    tempo = pesoRacao // 215000
    print("O tempo que o saco de ração vai durar, é: ", tempo)