print("Validação de Semha")

senha = 123456
inserir_senha = int(input("Digite sua senha: "))

while inserir_senha != senha:
    print("Senha incorreta Tente Novamente")
    inserir_senha = int(input("Digite sua senha novamente: "))
    print("Acesso Permitido!")
