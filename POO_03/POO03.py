#Crie um programa que liste os funcionários de determinado sexo,
#informado pelo usuário.

from FakeDB import FakeDB

DB = FakeDB()
DB.gerarFuncionarios()

sexo = input("Insira 'M' para Masculino, ou 'F' para Feminino: ")

for item in DB.listFuncionarios:
     if (item.sexo == sexo):
         print(item.nome + " " + item.sobrenome)
