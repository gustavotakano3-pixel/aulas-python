class ContaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo

    def get_titular(self):
        senha = 1234
        senha_digitada = int(input("Digite a sua senha: "))

        if senha == senha_digitada:
        return self.titular
    else:
        return 'Senha incorreta'


def set_titular(self, novo_titular):
    senha = 1234
    senha_digitada = int(input("Digite a sua senha: "))


    else:


conta_banco = ContaBancaria('Gustavo', 10000)
print(conta_banco.get_titular)
print(conta_banco.get_titular()