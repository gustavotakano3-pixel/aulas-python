print("Menu da Lanchonete")

id_produto = int(input("Digite o Id do produto (de 1 a 4): "))

match id_produto: #espera um num
    case 1:
        print("Cachorro-quente | R$ 10,00")
    case 2:
        print("Hambúrguer | R$ 15,00")
    case 3:
        print("Batata Frita | R$ 5,00")
    case 4:
        print("Refrigerante | R$ 5,00")
