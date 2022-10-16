#Crie um programa que liste os funcionários pelo nome, utilizando as 3
#primeiras letras do nome, informadas pelo usuário. Por exemplo, procure todos
#funcionários cujo nome comece com as letras MAR.

from FakeDB import FakeDB

DB = FakeDB()
DB.gerarFuncionarios ()

buscarnome = input("Insira as 3 primeiras letras: ")
for item in DB.listFuncionarios:
     if (item.nome.lower().startswith(buscarnome)):
        print(item.nome + " " + item.sobrenome)
