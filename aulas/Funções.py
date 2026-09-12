# CONHECENDO FUNÇOES NO PYTHON
# retorna um valor -> precisar desse valor
def soma():
    print("Fazendo uma soma.")
    numero1 = int(input('Numero 1: '))
    numero2 = int(input('Numero 2: '))
    return numero1 + numero2
# função vazia -> não retorna nada, mas executa algo
def subtracao():
    print("Fazendo uma subtração.")
    numero1 = int(input('Numero 1: '))
    numero2 = int(input('Numero 2: '))
    print(numero1 - numero2)
    return

def olaUsuario(nome):
    print(f"Olá {nome}")
    # ARQUIVO TesteFuncao.py
    #      biblioteca
    from aulas.Funcoes import soma, olaUsuario  # hierarquia

    olaUsuario("João")

    while True:
        valor = soma()
        print(valor)
        opcao = input("Quer finalizar? y/n")
        if opcao == 'y':
            break
    print("Finalizando execução.")  # parâmetro