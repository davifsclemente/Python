idade = int(input("Informe sua idade: "))
altura = float(input("Informe sua altura: "))
idioma = int(input("Quantos idiomas você fala: "))

if idade >= 24 and altura >= 1.70 and idioma >= 2:
    print("Você atende aos requisitos para essa vaga.")
else:
    print("Você não atende aos requisitos para essa vaga")