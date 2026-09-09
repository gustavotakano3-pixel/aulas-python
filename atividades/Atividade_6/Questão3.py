print("Somador de Números")

soma = 0
numero = int(input("Digite um número inteiro:"))

while numero != 0:
    soma += numero
    numero = int(input("Digite outro número inteiro:"))

print("Soma dos números é igual a:", soma)