from Pessoa import Pessoa

class Aluno(Pessoa):
    def __init__(self, nome, snome, email, tel, n_matricula, curso):
        super().__init__(nome, snome, email, tel)
        self.n_matricula = n_matricula
        self.curso = curso
    
    def ExibirN_matricula(self):
        return "Numero de matricula: " + self.n_matricula + "curso: " + self.curso

Aluno1 = Aluno(
    nome='José',
    snome='ferreira',
    email='jose123@gmail.com',
    tel='11 88551-6007',
    curso = "DSM",
    n_matricula = "213421321"
    )

print(Aluno1.ExibirNome_Completo())
print(Aluno1.ExibirN_matricula())