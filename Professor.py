from Pessoa import Pessoa

class Professor(Pessoa):
    def __init__(self, nome, snome, email, tel, salario):
        super().__init__(nome, snome, email, tel)
        self.salario = salario
    
    def ExibirTipoSalario(self):
        if self.salario > 4000:
            return "Sálario acima da media"
        else:
            return "Salario abaixo da media"
        
prof1 = Professor(
    nome="Maria",
    snome="Santos",
    email="maria123@gmail.com",
    tel="11 99661-7007",
    salario=5200
)

print(prof1.ExibirNome_Completo())
print(prof1.ExibirTipoSalario())