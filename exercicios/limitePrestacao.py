salTotal = float(input("Informe o salário bruto: "))
valorPrestacao = float(input("Informe o valor da prestação: "))
limite = salTotal * (30 / 100)

if valorPrestacao > limite:
    print("Você não pode fazer um empréstimo")
else:
    print("Você pode fazer um empréstimo")