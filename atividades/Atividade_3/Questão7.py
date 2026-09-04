print("O formulário de Doação de Sangue")

idade = int(input("Digite sua idade:"))

peso = int(input("Digite seu peso:"))

idade_certa = idade >= 16 and idade <= 69

peso_certo = peso >= 50

print("Você pode doar?",idade_certa and peso_certo)
      