from Funcionario import Funcionarios
import random
from datetime import date


class FakeDB:
    listFuncionarios = []

    def gerarFuncionarios(self):
        funcionarioList = []

        funcionarioList.append(Funcionarios(len(funcionarioList) + 1, "Marcelo", "Santos", "M", date(year=2000, month=random.randrange(1, 12), day=random.randrange(1, 28))))
        funcionarioList.append(Funcionarios(len(funcionarioList) + 1, "Junior", "Silva", "M", date(year=2000, month=random.randrange(1, 12), day=random.randrange(1, 28))))
        funcionarioList.append(Funcionarios(len(funcionarioList) + 1, "Cezar", "Souza", "M", date(year=2003, month=random.randrange(1, 12), day=random.randrange(1, 28))))
        funcionarioList.append(Funcionarios(len(funcionarioList) + 1, "Janio", "Quadros", "M", date(year=random.randrange(1989, 2003), month=random.randrange(1, 12), day=random.randrange(1, 28))))
        funcionarioList.append(Funcionarios(len(funcionarioList) + 1, "Camilo", "Jose", "M", date(year=random.randrange(1989, 2003), month=random.randrange(1, 12), day=random.randrange(1, 28))))
        funcionarioList.append(Funcionarios(len(funcionarioList) + 1, "Peter", "Carvalho", "M", date(year=random.randrange(1989, 2003), month=random.randrange(1, 12), day=random.randrange(1, 28))))
        funcionarioList.append(Funcionarios(len(funcionarioList) + 1, "Felipe", "Figueiredo", "M", date(year=random.randrange(1989, 2003), month=random.randrange(1, 12), day=random.randrange(1, 28))))
        funcionarioList.append(Funcionarios(len(funcionarioList) + 1, "Bento", "Peron", "M", date(year=random.randrange(1989, 2003), month=random.randrange(1, 12), day=random.randrange(1, 28))))
        funcionarioList.append(Funcionarios(len(funcionarioList) + 1, "Carlos", "Silveira", "M", date(year=random.randrange(1989, 2003), month=random.randrange(1, 12), day=random.randrange(1, 28))))
        funcionarioList.append(Funcionarios(len(funcionarioList) + 1, "Fernando", "Melo", "M", date(year=random.randrange(1989, 2003), month=random.randrange(1, 12), day=random.randrange(1, 28))))
        funcionarioList.append(Funcionarios(len(funcionarioList) + 1, "Mario", "Junqueira", "M", date(year=random.randrange(1989, 2003), month=random.randrange(1, 12), day=random.randrange(1, 28))))
        funcionarioList.append(Funcionarios(len(funcionarioList) + 1, "Marcos", "Medeiros", "M", date(year=random.randrange(1989, 2003), month=random.randrange(1, 12), day=random.randrange(1, 28))))
        funcionarioList.append(Funcionarios(len(funcionarioList) + 1, "Luke", "LoveLand", "M", date(year=random.randrange(1989, 2003), month=random.randrange(1, 12), day=random.randrange(1, 28))))
        funcionarioList.append(Funcionarios(len(funcionarioList) + 1, "Caio", "Castro", "M", date(year=random.randrange(1989, 2003), month=random.randrange(1, 12), day=random.randrange(1, 28))))
        funcionarioList.append(Funcionarios(len(funcionarioList) + 1, "Firmino", "Pereira", "M", date(year=random.randrange(1989, 2003), month=random.randrange(1, 12), day=random.randrange(1, 28))))
        funcionarioList.append(Funcionarios(len(funcionarioList) + 1, "Jacinto", "Solan", "M", date(year=random.randrange(1989, 2003), month=random.randrange(1, 12), day=random.randrange(1, 28))))
        funcionarioList.append(Funcionarios(len(funcionarioList) + 1, "Felca", "Lopes", "M", date(year=random.randrange(1989, 2003), month=random.randrange(1, 12), day=random.randrange(1, 28))))
        funcionarioList.append(Funcionarios(len(funcionarioList) + 1, "Luis", "Siqueira", "M", date(year=random.randrange(1989, 2003), month=random.randrange(1, 12), day=random.randrange(1, 28))))
        funcionarioList.append(Funcionarios(len(funcionarioList) + 1, "Jonatan", "Lima", "M", date(year=random.randrange(1989, 2003), month=random.randrange(1, 12), day=random.randrange(1, 28))))
        funcionarioList.append(Funcionarios(len(funcionarioList) + 1, "Vinicius", "Cortes", "M", date(year=random.randrange(1989, 2003), month=random.randrange(1, 12), day=random.randrange(1, 28))))
        funcionarioList.append(Funcionarios(len(funcionarioList) + 1, "Samuel", "Cabron", "M", date(year=random.randrange(1989, 2003), month=random.randrange(1, 12), day=random.randrange(1, 28))))
        funcionarioList.append(Funcionarios(len(funcionarioList) + 1, "Marcelo", "Ferreira", "M", date(year=random.randrange(1989, 2003), month=random.randrange(1, 12), day=random.randrange(1, 28))))
        funcionarioList.append(Funcionarios(len(funcionarioList) + 1, "Hugo", "Duarte", "M", date(year=random.randrange(1989, 2003), month=random.randrange(1, 12), day=random.randrange(1, 28))))
        funcionarioList.append(Funcionarios(len(funcionarioList) + 1, "Felipe", "Pedra", "M", date(year=random.randrange(1989, 2003), month=random.randrange(1, 12), day=random.randrange(1, 28))))
        funcionarioList.append(Funcionarios(len(funcionarioList) + 1, "Thiago", "Dudu", "M", date(year=random.randrange(1989, 2003), month=random.randrange(1, 12), day=random.randrange(1, 28))))
        funcionarioList.append(Funcionarios(len(funcionarioList) + 1, "Eduarda", "Duarte", "F", date(year=random.randrange(1989, 2003), month=random.randrange(1, 12), day=random.randrange(1, 28))))
        funcionarioList.append(Funcionarios(len(funcionarioList) + 1, "Adriana", "Figueiro", "F", date(year=random.randrange(1989, 2003), month=random.randrange(1, 12), day=random.randrange(1, 28))))
        funcionarioList.append(Funcionarios(len(funcionarioList) + 1, "Maria", "Rocha", "F", date(year=random.randrange(1989, 2003), month=random.randrange(1, 12), day=random.randrange(1, 28))))
        funcionarioList.append(Funcionarios(len(funcionarioList) + 1, "Tainara", "Monteiro", "F", date(year=random.randrange(1989, 2003), month=random.randrange(1, 12), day=random.randrange(1, 28))))
        funcionarioList.append(Funcionarios(len(funcionarioList) + 1, "Felipa", "Cunha", "F", date(year=random.randrange(1989, 2003), month=random.randrange(1, 12), day=random.randrange(1, 28))))
        funcionarioList.append(Funcionarios(len(funcionarioList) + 1, "Melissa", "Lima", "F", date(year=random.randrange(1989, 2003), month=random.randrange(1, 12), day=random.randrange(1, 28))))
        funcionarioList.append(Funcionarios(len(funcionarioList) + 1, "Marcela", "Ferreiro", "F", date(year=random.randrange(1989, 2003), month=random.randrange(1, 12), day=random.randrange(1, 28))))
        funcionarioList.append(Funcionarios(len(funcionarioList) + 1, "Suelen", "Nobriga", "F", date(year=random.randrange(1989, 2003), month=random.randrange(1, 12), day=random.randrange(1, 28))))
        funcionarioList.append(Funcionarios(len(funcionarioList) + 1, "Luara", "Pires", "F", date(year=random.randrange(1989, 2003), month=random.randrange(1, 12), day=random.randrange(1, 28))))
        funcionarioList.append(Funcionarios(len(funcionarioList) + 1, "Zulema", "Nogueira", "F", date(year=random.randrange(1989, 2003), month=random.randrange(1, 12), day=random.randrange(1, 28))))
        funcionarioList.append(Funcionarios(len(funcionarioList) + 1, "Marie", "Jane", "F", date(year=random.randrange(1989, 2003), month=random.randrange(1, 12), day=random.randrange(1, 28))))
        funcionarioList.append(Funcionarios(len(funcionarioList) + 1, "Hellen", "Gazaroli", "F", date(year=random.randrange(1989, 2003), month=random.randrange(1, 12), day=random.randrange(1, 28))))
        funcionarioList.append(Funcionarios(len(funcionarioList) + 1, "Eliana", "Pereira", "F", date(year=random.randrange(1989, 2003), month=random.randrange(1, 12), day=random.randrange(1, 28))))
        funcionarioList.append(Funcionarios(len(funcionarioList) + 1, "Luana", "Rodrigues", "F", date(year=random.randrange(1989, 2003), month=random.randrange(1, 12), day=random.randrange(1, 28))))
        funcionarioList.append(Funcionarios(len(funcionarioList) + 1, "Carla", "Fernandes", "F", date(year=random.randrange(1989, 2003), month=random.randrange(1, 12), day=random.randrange(1, 28))))
        funcionarioList.append(Funcionarios(len(funcionarioList) + 1, "Mariana", "Barros", "F", date(year=random.randrange(1989, 2003), month=random.randrange(1, 12), day=random.randrange(1, 28))))
        funcionarioList.append(Funcionarios(len(funcionarioList) + 1, "Larissa", "Rosilda", "F", date(year=random.randrange(1989, 2003), month=random.randrange(1, 12), day=random.randrange(1, 28))))
        funcionarioList.append(Funcionarios(len(funcionarioList) + 1, "Roseane", "Peruada", "F", date(year=random.randrange(1989, 2003), month=random.randrange(1, 12), day=random.randrange(1, 28))))
        funcionarioList.append(Funcionarios(len(funcionarioList) + 1, "Katia", "Vargas", "F", date(year=random.randrange(1989, 2003), month=random.randrange(1, 12), day=random.randrange(1, 28))))
        funcionarioList.append(Funcionarios(len(funcionarioList) + 1, "Morticia", "Gomes", "F", date(year=random.randrange(1989, 2003), month=random.randrange(1, 12), day=random.randrange(1, 28))))
        funcionarioList.append(Funcionarios(len(funcionarioList) + 1, "Paula", "Pauleti", "F", date(year=random.randrange(1989, 2003), month=random.randrange(1, 12), day=random.randrange(1, 28))))
        funcionarioList.append(Funcionarios(len(funcionarioList) + 1, "Laura", "Menegin", "F", date(year=random.randrange(1989, 2003), month=random.randrange(1, 12), day=random.randrange(1, 28))))
        funcionarioList.append(Funcionarios(len(funcionarioList) + 1, "Jenifer", "Lopes", "F", date(year=random.randrange(1989, 2003), month=random.randrange(1, 12), day=random.randrange(1, 28))))
        funcionarioList.append(Funcionarios(len(funcionarioList) + 1, "Ayla", "De armas", "F", date(year=random.randrange(1989, 2003), month=random.randrange(1, 12), day=random.randrange(1, 28))))
        funcionarioList.append(Funcionarios(len(funcionarioList) + 1, "Sofia", "Negrine", "F", date(year=random.randrange(1989, 2003), month=random.randrange(1, 12), day=random.randrange(1, 28))))

        self.listFuncionarios = funcionarioList


