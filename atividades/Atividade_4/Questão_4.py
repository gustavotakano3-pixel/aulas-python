print("O Teste do Saldo Bancário")
saldo_atual = float(input("Digite seu Saldo:"))
saque = float(input("Digite o valor do Seu Saque:"))
saldo_pos_saque = saldo_atual - saque
if saque <= saldo_atual:
    print("Saque Realizado Com uucesso!:","Saldo atual",saldo_pos_saque)
else:
    print("Saldo Insuficiente para Realizar esta Operação")

    