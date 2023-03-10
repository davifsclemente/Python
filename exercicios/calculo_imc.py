idade = int(input("Informe sua idade: "))
peso = float(input("Informe o seu peso: "))

if idade >= 18 and peso > 50.0 or idade <= 65 and peso > 50:
    print("Você pode ser um doador")
else:
    print("Você não pode doar")