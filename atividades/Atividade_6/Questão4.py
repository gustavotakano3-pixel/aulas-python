print("Menu Interativo")

opcao = int(input("Escolha uma opção:"))
while opcao != 2:
    if opcao == 1:
        print("Seja Bem Vindo(a)")
    else:
        print("Opção Inválida")
    opcao = int(input("Escolha outra opção:"))
print("Programa encerrado")