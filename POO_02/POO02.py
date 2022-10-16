#Crie um programa que liste os funcionários que fazem aniversário em
#determinado ano, informado pelo usuário.


from FakeDB import FakeDB

DB = FakeDB()
DB.gerarFuncionarios()

ano = int(input("Insira o ano de Nascimento: "))

for item in DB.listFuncionarios:
     if (item.dataNascimento.year == ano):
         print(item.nome + " " + item.sobrenome)