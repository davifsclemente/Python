"""
    Um aluno deseja saber qual a porcentagem de faltas que ele tem em cada disciplina.
    Ajude este aluno para que ele sempre possa calcular sua porcentagem de faltas. Para
    isso, escreva um programa em Python que leia a carga horária da disciplina e a
    quantidade de horas de faltas acumuladas, calcule a porcentagem e a imprima na tela.
"""

cargaHrTotal = int(input("Informe a carga horária total: "))
cargaHrDisci = int(input("Informe a carga horária da disciplina: "))
qtdHrAcul = int(input("Informe a quantidade de horas perdida: "))
porcentagem = ((cargaHrDisci - qtdHrAcul) / cargaHrTotal * 100)

print("Você faltou: ", porcentagem, "%")