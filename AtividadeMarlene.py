from datetime import datetime

class Veiculo:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano

    def exibir_dados(self):
        print("Marca:", self.marca)
        print("Modelo:", self.modelo)
        print("Ano:", self.ano)

    def verificar_idade(self):
        ano_atual = datetime.now().year
        idade = ano_atual - self.ano

        if idade <= 3:
            print("Classificaçao: Novo")
        elif idade <= 10:
            print("Classificaçao: Seminovo")
        else:
            print("Classificaçao: Antigo")


# Parte 2
class Carro(Veiculo):
    def __init__(self, marca, modelo, ano, numero_portas, tipo_combustivel):
        super().__init__(marca, modelo, ano)
        self.numero_portas = numero_portas
        self.tipo_combustivel = tipo_combustivel

    def info_carro(self):
        print("Carro")
        self.exibir_dados()
        print("Portas:", self.numero_portas)
        print("Combutível:", self.tipo_combustivel)
        self.verificar_idade()


# Parte 3
class Moto(Veiculo):
    def __init__(self, marca, modelo, ano, cilindradas, tipo_partida):
        super().__init__(marca, modelo, ano)
        self.cilindradas = cilindradas
        self.tipo_partida = tipo_partida

    def info_moto(self):
        print("\nMoto")
        self.exibir_dados()
        print("Cilinradas:", self.cilindradas)
        print("Partida:", self.tipo_partida)
        self.verificar_idade()


# Parte 4

carro1 = Carro("Toyota", "Corolla", 2022, 4, "Flex")
moto1 = Moto("Honda", "CG 160", 2021, 160, "Elétrica")

carro1.info_carro()
moto1.info_moto()