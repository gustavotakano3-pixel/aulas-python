class Carro:
    def __init__(self, marca, modelo, cor, ano, fabricante):
        self.marca = marca
        self.modelo = modelo
        self.cor = cor
        self.ano = ano
        self.fabricante = fabricante

    def ligar(self):
        return f"{self.marca} {self.modelo} está ligado "

    def acelerar(self):
        return f"{self.marca} {self.modelo} está acelerando "

    def frear(self):
        return f"{self.marca} {self.modelo} está freando "

    def __str__(self):
        return f"Marca: {self.marca} | Modelo: {self.modelo} | Cor: {self.cor} | Ano: {self.ano} | Fabricante: {self.fabricante}"

carro1 = Carro("Toyota", "Corolla", "prata", 2022, "Toyota")
carro2 = Carro("Honda", "Civic", "preto", 2023, "Honda")
carro3 = Carro("Volkswagen", "Golf", "Branco", 2020, "Volkswagen")
carro4 = Carro("Chevrolet", "Onix", "vermelho", 2024, "Chevrolet")
carro5 = Carro("Ford", "Mustang", "azul", 2021, "Ford")

carros = [carro1, carro2, carro3, carro4, carro5]

for carro in carros:
    print(carro)