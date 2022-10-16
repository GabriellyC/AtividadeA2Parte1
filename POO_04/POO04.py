#Crie um programa que sorteie e liste um determinado número de
#funcionários. Por exemplo, sortear aleatoriamente e listar 5 funcionários, SEM
#REPETIR.

from FakeDB import FakeDB
import random

num = int(input("Insira a quantidade de Funcionários: "))

DB = FakeDB()
DB.gerarFuncionarios()

lista = []
while len(lista) < num:
    func = random.choice(DB.listFuncionarios)

    ilista = True

    for item in lista:
        if(lista.__contains__(func)):
            ilista = False

    if(ilista):
        lista.append(func)

for func in lista:
    print(func.nome + " " + func.sobrenome)




