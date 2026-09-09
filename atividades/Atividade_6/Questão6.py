print("Jogo da Adivinhação")

numero_secreto = 27

opcao = int(input("Insira o numero secreto: "))

tentativas = 1

while opcao != numero_secreto:
    print("Número errado")
    opcao = int(input("Insira outro numero: "))
    tentativas += 1
print("Você Acertou!")
print("Número de Tentativas",tentativas)

