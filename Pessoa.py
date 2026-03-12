class Pessoa:
    def __init__(self,nome,snome,email,tel):
        self.nome = nome
        self.snome = snome
        self.email = email
        self.tel = tel
    
    def ExibirNome_Completo(self):
        return "Nome Completo: " + self.nome + " " + self.snome
    
p1 = Pessoa(nome='Maria', snome='Santos', email='maria123@gmail.com', tel='11 99661-7007')
p2 = Pessoa(nome='José', snome='ferreira', email='jose123@gmail.com', tel='11 88551-6007')

print(p1.ExibirNome_Completo())
print(p2.ExibirNome_Completo())
