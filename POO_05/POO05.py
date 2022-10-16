#Crie um programa que busque e liste os funcionários que tenham as 3
#letras determinadas no sobrenome, informadas pelo usuário. Por exemplo, procure
#todos funcionários que tenham as letras SAN no sobrenome.


from FakeDB import FakeDB

DB = FakeDB()
DB.gerarFuncionarios ()

buscarsobrenome = input("Insira as 3 primeiras letras do sobrenome: ")
for item in DB.listFuncionarios:
     if (item.sobrenome.lower().startswith(buscarsobrenome)):
        print(item.nome + " " + item.sobrenome)